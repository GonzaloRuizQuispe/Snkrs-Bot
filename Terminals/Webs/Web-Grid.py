import requests
from bs4 import BeautifulSoup as b
import mysql.connector
from mysql.connector import Error

from Talles import Talles_Grid

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
            
            #1° Se Ejecuta La Busqueda De La Tabla De Productos Grid
            cursor.execute("SELECT * FROM productos_grid")

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
                    
                    #Extracción De La Ubicación Del Post
                    Post_Partition = 'div'
                    Post_Class = 'class'
                    Post_Name_Tag = 'row product-details'

                    #Extracción De La Ubicación Del Nombre
                    Name_Partition = 'div'
                    Name_Class = 'class'
                    Name_Name_Tag = 'product-name'

                    #Extracción De La Ubicación Del Precio
                    Precio_Partition = 'strong'
                    Precio_Class = 'class'
                    Precio_Name_Tag = 'skuBestPrice'

                    #Extracción De La Ubicación De La Imagen
                    Img_Partition = 'img'
                    Img_Class = 'id'
                    Img_Name_Tag = 'image-main'

                    #Extraccion De Datos
                    post = soup.find(''+Post_Partition+'',{''+Post_Class+'':''+Post_Name_Tag+''})
                    Nombre = post.find(''+Name_Partition+'',{''+Name_Class+'':''+Name_Name_Tag+''})
                    Precio = post.find(''+Precio_Partition+'',{''+Precio_Class+'':''+Precio_Name_Tag+''})
                    URL_IMG = post.find(''+Img_Partition+'',{''+Img_Class+'':''+Img_Name_Tag+''}).get('src')

                    #Extracción Talles En Script
                    r = soup.find(lambda script: script.name == 'script' and 'var skuJson_0' in str(script))
                    Talles = ""

                    for data in Talles_Grid.talles_grid(str(r)):
                        for a in data['dimensionsMap']['Talle']:
                            Talles += a+" ┋ "

                    #Se Insertan Los Datos En La DB
                    if fila[5] == 'Delete':
                        cursor.execute("UPDATE productos_grid SET Nombre='"+str(Nombre.text)+"',Precio="+str(Precio.text[1:-3])+",URL_IMG='"+str(URL_IMG)+"',Cambios='StockOn',Talles='"+Talles[:-3]+"' WHERE ID_Producto="+str(fila[0]))
                    
                    elif fila[6] != Talles[:-3]:
                        cursor.execute("UPDATE productos_grid SET Nombre='"+str(Nombre.text)+"',Precio="+str(Precio.text[1:-3])+",URL_IMG='"+str(URL_IMG)+"',Cambios='Talles',Talles='"+Talles[:-3]+"' WHERE ID_Producto="+str(fila[0]))

                    elif fila[5] == 'Talles':
                        print(fila[6])
                        print("Esperando Cambio De Programa Notificaciónes")

                    elif fila[5] == 'StockOn':
                        print("Esperando Cambio De Programa Notificaciónes")

                    else:
                        cursor.execute("UPDATE productos_grid SET Nombre='"+str(Nombre.text)+"',Precio="+str(Precio.text[1:-3])+",URL_IMG='"+str(URL_IMG)+"',Cambios='Nuevo',Talles='"+Talles[:-3]+"' WHERE ID_Producto="+str(fila[0]))

                    #Se Guardan Los Cambios En La DB
                    connection.commit()
                
                #De No Encontrar "Post" Se Almacena De Manera Diferente
                except AttributeError:

                    #Si Ya Se Encuentra Eliminado Se Saltea Y Notifica
                    if fila[5] == 'Delete':
                        print("En Espera De Cambios")

                    #Si No Se Encuentra Eliminado Es Agregado Es Actualizado En Cambios Como 'Delete'
                    else:
                        cursor.execute("UPDATE productos_grid SET Cambios='Delete' WHERE ID_Producto="+str(fila[0]))

                    #Se Guardan Los Cambios En La DB
                    connection.commit()

    #Al Romper El Loop Manual Mente Envia Mensaje Avisando
    except Error as ex:
        print("Error durante la conexion: ",ex)

    except KeyboardInterrupt:
        print("El Programa Ha Finalizado")
        break