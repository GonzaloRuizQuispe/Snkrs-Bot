import requests
from bs4 import BeautifulSoup as b

url = 'https://www.grid.com.ar/botitas-jordan-air-xxxvi-moda-hombre-3160255/p'

html = requests.get(url)
contenido = html.content
soup = b(contenido,"lxml")

titulo_destacado = soup.find("div",{"class":"product-name"})
print(titulo_destacado.text)
precio_destacado = soup.find("strong",{"class":"skuBestPrice"})
print(precio_destacado.text)
talles_destacado = soup.find("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div/section/div[1]/div[1]/div/div[2]/div/div[1]/img")
print(talles_destacado)
