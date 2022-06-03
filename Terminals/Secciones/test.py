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

url = 'https://www.tiendafuencarral.com.ar/tienda-fuencarral/PUMA/CALZADO/ZAPATILLAS?map=c,b,c,c##page=2'

html = requests.get(url,headers=headers)
contenido = html.content
soup = b(contenido,"lxml")

post = soup.find('article',{'class':'productos'})

for box in post.findAll('li',{'class':'tienda-fuencarral last'}):
    new_link = box.find('a',{'class':'productImage'}).get('href')
    print(new_link)