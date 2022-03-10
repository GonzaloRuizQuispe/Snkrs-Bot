import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Cargar Ruta Excel
mensaje = open ('ruta_excel.txt','r')
ruta_xlsx = mensaje.read()

#Cargar Ruta URL
mensaje = open('ruta_url.txt','r')
ruta_url = mensaje.read()

# Cargar Excel
xlsx = r''+ruta_xlsx+''

# Leer Excel
df = pandas.read_excel(xlsx)

# Guardar Datos Del Excel
user = df['email'][0]
password = df['password'][0]

# Pagina A Usar
url = ''+ruta_url+''

# Selectores
selec_user = '#i0116'
button_login1= '#idSIButton9'
selec_password = '#i0118'
button_login = '#idSIButton9'

# Abrir Navegador
driver = webdriver.Chrome()

# Maximixar Pestaña
driver.maximize_window()

# Abrir Pagina Url
driver.get(url)

# Acciones En La Pagina
# 1 Poner Usuario
driver.find_element_by_css_selector(selec_user).send_keys(user)
# Boton 1
driver.find_element_by_css_selector(button_login1).click()

# 2 Poner Contraseña 
driver.find_element_by_css_selector(selec_password).send_keys(password)
# Esperar
time.sleep(2)

# 3 Dar A Boton Iniciar

driver.find_element_by_css_selector(button_login).click()

# 4 Esperar A Que Cargue

time.sleep(7)

# 5 Cerrar

driver.quit()