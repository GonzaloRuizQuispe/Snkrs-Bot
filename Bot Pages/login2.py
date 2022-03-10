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

#Leer Excel
excel_credentials = r''+ruta_xlsx+''
df = pandas.read_excel(excel_credentials)

#Botones
path_busqueda = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
path_boton_busqueda = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button'
path_musica = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]'

#Acciones
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(ruta_url)

for i in df.index:
    cancion = str(df['cancion'][i])
    
    #Paso 1
    driver.find_element_by_xpath(path_busqueda).send_keys(cancion)
    driver.find_element_by_xpath(path_boton_busqueda).click()

    #Esperar Que Cargue
    wait = WebDriverWait(driver,10)
    wait.until(ec.visibility_of_element_located((By.XPATH, path_musica)))
    
    #Paso 2
    driver.find_element_by_xpath(path_musica).click()
    
    #Paso 3
    time.sleep(50)
    
    #Paso 4
    driver.find_element_by_xpath(path_busqueda).clear()
driver.quit()