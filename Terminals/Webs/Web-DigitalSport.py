import requests
from bs4 import BeautifulSoup as b
import mysql.connector
from mysql.connector import Error

#Registro En Pagina
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"DNT":"1"
}

#Conectarse A La DB
connection = mysql.connector.connect(
host = 'localhost',
port = 3306,
user = 'root',
password = 'Pool!Live45427752',
db = 'snkrs'
)

#Repeticion Infinita
while True:

    #Se Crea La Excepion Para Romper El Loop Manual Mente
    try:


        #Si Se Conecta Envia Un Mensaje De Confirmación
        if connection.is_connected():
            print("Conexion Exitosa SNKRS WEB GRID")

            #Conectado Se Declara Cursor Para Realizar Acciones Dentro De La DB
            cursor = connection.cursor()

            #1° Prueba Mostrando El Nombre De La DB
            cursor.execute("SELECT database();")
            registro = cursor.fetchone()
            print("Conectado a la BD:",registro,"\n")

            #De Aca En Adelante Se Puede Empezar A Leer/Escribir La DB
            
            #1° Se Ejecuta La Busqueda De La Tabla De Productos digitalsport
            cursor.execute("SELECT * FROM productos_digitalsport")

            #Se Seleccionan Todos Los Datos
            cantidad_f = cursor.fetchall()

            #2° Se Inicia La Repeticion Por Cantidad De Datos
            for fila in cantidad_f:

                #Se Establece La URL Del Producto Ubicada En El La Columna 3
                url = fila[4]
            
                #Se Entra A La Pagina
                html = requests.get(url,headers=headers)
                contenido = html.content
                soup = b(contenido,"lxml")

                #Se Crea Una Excepcion Si No Se Ecuentra "Post" Que Es El Espacio Donde Se Ubica El Articulo
                try:

                    #Extraccion De Datos
                    post = soup.find('div',{'class':'product_center'})
                    Nombre = post.find('h1')
                    Precio = post.find('span',{'class':'price'})
                    URL_IMG = "https://www.digitalsport.com.ar"+post.find('img',{'class':'media'}).get('src')

                    Talles = ""

                    Box_Size = post.find('ul',{'id':'sizes'})
                    for Size in Box_Size.findAll('div',{'class':'arg'}):
                        Talles += Size.text[3:]+" ┋ "

                    #Se Insertan Los Datos En La DB
                    if fila[5] == 'Delete':
                        cursor.execute("UPDATE productos_digitalsport SET Nombre='"+str(Nombre.text)+"',Precio="+str(Precio.text[1:])+",URL_IMG='"+str(URL_IMG)+"',Cambios='StockOn',Talles='"+Talles[:-3]+"',Hora=CURRENT_TIMESTAMP() WHERE ID_Producto="+str(fila[0]))
                    
                    elif fila[6] != Talles[:-3]:
                        cursor.execute("UPDATE productos_digitalsport SET Nombre='"+str(Nombre.text)+"',Precio="+str(Precio.text[1:])+",URL_IMG='"+str(URL_IMG)+"',Cambios='Talles',Talles='"+Talles[:-3]+"',Hora=CURRENT_TIMESTAMP() WHERE ID_Producto="+str(fila[0]))

                    elif fila[5] == 'Talles':
                        print("Esperando Cambio De Programa Notificaciónes")

                    elif fila[5] == 'StockOn':
                        print("Esperando Cambio De Programa Notificaciónes")

                    else:
                        cursor.execute("UPDATE productos_digitalsport SET Nombre='"+str(Nombre.text)+"',Precio="+str(Precio.text[1:])+",URL_IMG='"+str(URL_IMG)+"',Cambios='Nuevo',Talles='"+Talles[:-3]+"',Hora=CURRENT_TIMESTAMP() WHERE ID_Producto="+str(fila[0]))

                    #Se Guardan Los Cambios En La DB
                    connection.commit()
                
                #De No Encontrar "Post" Se Almacena De Manera Diferente
                except AttributeError:

                    #Si Ya Se Encuentra Eliminado Se Saltea Y Notifica
                    if fila[5] == 'Delete':
                        print("En Espera De Cambios")

                    #Si No Se Encuentra Eliminado Es Agregado Es Actualizado En Cambios Como 'Delete'
                    else:
                        cursor.execute("UPDATE productos_digitalsport SET Cambios='Delete' WHERE ID_Producto="+str(fila[0]))

                    #Se Guardan Los Cambios En La DB
                    connection.commit()

    #Al Romper El Loop Manual Mente Envia Mensaje Avisando
    except Error as ex:
        print("Error durante la conexion: ",ex)

    except KeyboardInterrupt:
        print("El Programa Ha Finalizado")
        input("Esperando Entrada De Administrador\n")
        break