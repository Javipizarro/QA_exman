from selenium import webdriver
from requests import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager   #To automaticaly download the webdriver that suits our browser version
from selenium.webdriver.common.by import By
from time import sleep
from secret import email, password

option2 = Options()
option2.add_argument("--disable-notifications")

class TinderBot():
	def __init__(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option2)

	def login(self):
		self.driver.get('https://tinder.com')
		self.driver.maximize_window()
		self.driver.delete_all_cookies()
		sleep(2)
#		noCookies = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[2]/div/div/div[1]/div[2]/button')
		try:
			#noCookies = self.driver.find_element(By.XPATH, '//*[@id="q1272886408"]/div/div[2]/div/div/div[1]/div[2]/button')
			#noCookies.click()
			self.driver.find_element(By.XPATH, '//*[@id="o-1389276889"]/div/div[2]/div/div/div[1]/div[2]/button').click()
		except:
			pass
#		logInBtn = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
		logInBtn = self.driver.find_element(By.XPATH, '//*[@id="o-1389276889"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
		logInBtn.click()
#		self.driver.find_element(By.LINK_TEXT , 'https://tinder.onelink.me/9K8a/3d4abb81').click()
		sleep(1)
		fbBtn = self.driver.find_element(By.XPATH, '//*[@id="o1177309331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
		fbBtn.click()
		sleep(1)
		mainWindow = self.driver.window_handles[0]
		popup = self.driver.switch_to.window(self.driver.window_handles[1])
		sleep(1)
#		fbNoCookies = self.driver.find_element(By.XPATH, '//*[@id="u_0_a_Qt"]')
		fbNoCookies = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]')
		fbNoCookies.click()
		fbUserBox = self .driver.find_element(By.XPATH, '//*[@id="email"]')
		fbUserBox.send_keys(email)
		fbPasswordBox = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
		fbPasswordBox.send_keys(password)
		sleep(1)
		fbLoginBtn = self.driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
		fbLoginBtn.click()
#		sleep(2)
		self.driver.switch_to.window(mainWindow)
		sleep(5)
#		allowLocation = self.driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[1]')
#		allowLocation.click()
#		denyNotifications = self.driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[1]')
#		denyNotifications.click()
#		noEmailBtn = self.driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div[1]/div/div[2]/button[2]')
#		noEmailBtn.click()

#		allowNotifications = self.driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[1]')
#		allowNotifications.click()
		sleep(1)

	def like(self):
		try:
			likeBtn = self.driver.find_element(By.XPATH, '//*[@id="o-1389276889"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
		except Exception:
			try:
				likeBtn = self.driver.find_element(By.XPATH, '//*[@id="o-1389276889"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
			except Exception:
				return 0
		likeBtn.click()

	def dislike(self):
		try:
			dislikeBtn = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
		except Exception:
			try:
				dislikeBtn = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
			except Exception:
				return 0
		dislikeBtn.click()

	def notAddingTinderToHomeScreen(self): #Funciona correctamente (al menos al tamaño original)
		notAddBtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button[2]')
		notAddBtn.click()

	def	avoidOffer(self):
		try:
			closeOfferBtn = self.driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div[2]/button')
		except Exception:
				closeOfferBtn = self.driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div[2]/div/div[3]/button[2]')
		closeOfferBtn.click()

	def sendMessage(self): #No funciona cerrando la ventana de match!!
		self.driver.find_element(By.XPATH, '//*[@id="o1614562120"]').send_keys('Hola! Me ha encantado tu perfil. ¿Cómo te va?\n')
			
##		Capturar nombre y tal para personalizar mensaje
#		girlName = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/h1')
#		girlAge = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/span')
#		girlDistance = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div[4]/div[2]')

		messageArea = self.driver.find_element(By.XPATH, '//*[@id="u1353565419"]')
		messageArea.send_keys('Hola!')
		sendBtn = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button[2]/span')
		sendBtn.click()
		closeChatBtn = self.driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[1]/a/button')
		closeChatBtn.click()

	def auto_swipe(self):
		while True:
			sleep(0.5)
			try:
				self.like()
			except Exception:
				try:
					self.sendMessage()
				except Exception:
					try:
						self.notAddingTinderToHomeScreen()
					except Exception:
						try:
							self.avoidOffer()
						except Exception:
							print("New exception while auto_swipping\n")


bot = TinderBot()
bot.login()
bot.auto_swipe()
sleep(10)

#XPATH para la X del match //*[@id="o-1058905688"]/main/div/div[1]/div/div[4]/button/svg/path
#XPATH para el campo de escritura de la ventana de match //*[@id="o1614562120"]  (FUNCIONA A 24/8/2022)
#XPATH para el boton de send de la ventana de match //*[@id="o-1058905688"]/main/div/div[1]/div/div[3]/div[3]/form/button