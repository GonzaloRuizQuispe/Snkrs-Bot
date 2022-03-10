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

#Programa
while True:
    try:
        if connection.is_connected():
            print("Conexion Exitosa SNKRS SECCION GRID")

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM secciones_grid")
            cantidad_f = cursor.fetchall()

            for fila in cantidad_f:
                #Se Establece La url Con La Información Extraida De La DB
                url = fila[1]

                #Se Entra A La Pagina
                html = requests.get(url,headers=headers)
                contenido = html.content
                soup = b(contenido,"lxml")

                #Extraccion De Datos
                post = soup.find("div",{"class":"prateleira vitrine shelf"})
                box_productos = post.findAll("div",{"class":"prateleira vitrine shelf n1colunas"})
                    
                for box in box_productos:
                    for productos in box.findAll("li",{"class":"calzado-|-calzados---compra-calzado last"}):
                        new_link = productos.find("a",{"id":"imgOriginal"}).get('href')

                        cursor.execute("SELECT URL_WEB FROM productos_grid WHERE URL_WEB='"+new_link+"'")
                        old_link = cursor.fetchone()

                        if old_link == None:
                            cursor.execute("INSERT INTO productos_grid (URL_WEB) VALUES ('"+new_link+"')")
                            connection.commit()

                        else:
                            print("Esta seccion se encuentra actualizada")

    except Error as ex:
        print("Error durante la conexion: ",ex)

    except KeyboardInterrupt:
        print("El Programa Ha Finalizado")
        break