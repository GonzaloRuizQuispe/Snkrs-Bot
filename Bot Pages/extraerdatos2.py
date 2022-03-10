import requests
import xlsxwriter
from bs4 import BeautifulSoup as b

workbook = xlsxwriter.Workbook('snkrs.xlsx')
worksheet = workbook.add_worksheet("Zapatillas-Grid")
worksheet.write('A1','Producto')
worksheet.write('B1','Precio')
worksheet.write('C1','URL_IMG')
worksheet.write('D1','URL_Producto')

url = 'https://www.grid.com.ar/calzado/zapatillas/148?O=OrderByReleaseDateDESC&PS=24&map=c,c,productClusterIds'

## -------------------------
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"DNT":"1"
}
## -------------------------

html = requests.get(url,headers = headers)
contenido = html.content
soup = b(contenido,"lxml")

row = 1
for post in soup.findAll("div",{"class":"box-item"}):
    titulo = post.find("b",{"class":"product-name"})
    precio = post.find("span",{"class":"best-price"})
    url_img = post.find('img')['src']
    if precio is not None:
        #print(titulo.text)
        #print(precio.text)
        worksheet.write(row,0,titulo.text)
        worksheet.write(row,1,precio.text)
        worksheet.write(row,2,url_img)
        worksheet.write(row,3,url)
        row += 1

workbook.close()