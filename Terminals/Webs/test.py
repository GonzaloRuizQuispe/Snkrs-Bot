from turtle import pos
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

url = "https://www.digitalsport.com.ar/dionysos/prod/zapatillas-superstar-adidas-539125/"

html = requests.get(url,headers=headers)
contenido = html.content
soup = b(contenido,"lxml")

post = soup.find('div',{'class':'product_center'})
Nombre = post.find('h1').text
Precio = post.find('span',{'class':'price'}).text
URL_IMG = post.find('img',{'class':'media'}).get('src')

Talle = ""

Box_Size = post.find('ul',{'id':'sizes'})
for Size in Box_Size.findAll('div',{'class':'arg'}):
    Talle += Size.text[3:]+" ┋ "

print(Nombre,Precio,"https://www.digitalsport.com.ar"+URL_IMG,Talle)