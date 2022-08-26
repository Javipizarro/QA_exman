#	'Selenium' es una biblioteca para automatizaciones (en este caso para python)
#	Selenium es una biblioteca muy grande, por eso importamos la parte 'webdriver' de la misma
from selenium import webdriver

#	Estas siguientes son para instalar el driver de Chrome de manera automática.
#	El driver de Chrome es una extensión para chrome para poder interactuar con él vía software
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#	Esta es necesaria para que reconozca la palabra By en By.XPATH, por ejemplo
from selenium.webdriver.common.by import By

#	Para poder usar la función sleep
from time import sleep

#	La variable 'driver' almacena un objeto; este objeto resulta de llamar a la clase 'Chrome' de 'webdriver' abierto con el driver instalado desde ChormeDriveManager
#	Como resultado, abriremos un navegador Chrome con el que podremos interactuar mediante nuestro objeto 'driver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#	El método get de la clase Chrome, aplicado a nuestro objeto 'driver' hace que el navegador se dirija a la URL entre paréntesis
driver.get('https://www.wordreference.com/')

#	Esperamos a que cargue la página
sleep(2)

#	Buscamos la caja de búsqueda por su xpath
searchBox = driver.find_element(By.XPATH, '//*[@id="si"]')
#	le inyectamos texto
searchBox.send_keys('uncommon')
#	y le damos un retorno de carro para que busque como al pulsar 'intro'
searchBox.send_keys('\n')

#	Buscamos el botón de búsqueda PD: NO es necesario el botón de búsqueda si introducimos un retorno de carro al final del texto
#searchButton = driver.find_element(By.XPATH, '//*[@id="text_form"]/input[2]')
#	Hacemos click en él
#searchButton.click()

#	Cerramos el pop-up de las cookies con:
noCoockiesButton = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[2]/p')
noCoockiesButton.click()

#	Cuando acaba el programa sale automáticamente del navegador, le decimos que espere un poquito para poder ver el resultado
sleep(10)