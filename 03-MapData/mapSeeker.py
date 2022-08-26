from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.es/maps/")

cookiesBtn = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button')
cookiesBtn.click()

#searchBox = driver.find_element(By.XPATH, '//*[@id="searchbox"]')
searchBox = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
searchBox.send_keys('Cuenca')
searchBox.send_keys('\n')
#searchBtn = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
#searchBtn.click()
sleep(3)
directionBtn = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button')
directionBtn.click()
sleep(2)
locationBox = driver.find_element(By.XPATH, '//*[@id="sb_ifc51"]/input')
#locationBox = driver.find_element(By.XPATH, '//*[@id="sb_ifc50"]/input')
locationBox.send_keys('Plasencia')
locationBox.send_keys('\n')
sleep(6)
via1Name = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-title-0"]/span')
via1Time = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')
via1Distance = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div')
print("\nVia 1:\n" + via1Name.text + "\nTime:\t\t" + via1Time.text + "\nDistance:\t" + via1Distance.text + "\n")

via2Name = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-title-1"]/span')
via2Time = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-1"]/div[1]/div[1]/div[1]/div[1]/span[1]')
via2Distance = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-1"]/div[1]/div[1]/div[1]/div[2]/div')
print("\nVia 2:\n" + via2Name.text + "\nTime:\t\t" + via2Time.text + "\nDistance:\t" + via2Distance.text + "\n")

via3Name = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-title-2"]/span')
via3Time = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-2"]/div[1]/div[1]/div[1]/div[1]/span[1]')
via3Distance = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-2"]/div[1]/div[1]/div[1]/div[2]/div')
print("\nVia 3:\n" + via3Name.text + "\nTime:\t\t" + via3Time.text + "\nDistance:\t" + via3Distance.text + "\n")

sleep(10)