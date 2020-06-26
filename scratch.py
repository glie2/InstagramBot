import os
import time
import configparser
from selenium import webdriver




# print("hello world")

# config = configparser.ConfigParser()
# config.read('config_.ini')
# print(config['IG_AUTH']['USERNAME'])
# print(config['IG_AUTH']['PASSWORD'])

# print(config['IG_URLS']['LOGIN'])
# print(config['IG_URLS']['NAV_USER'])
# print(config['IG_URLS']['SEARCH_TAGS'])
# print(config.sections())

class Instagramb:

	def __init__(self, username, password):

		self.username = username
		self.password = password
		self.login_url = 'https://www.instagram.com/'
		mobile_emulation = {"deviceName" : "Pixel 2 XL"}
		self.chrome_options = webdriver.ChromeOptions()
		chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
		self.driver = webdriver.Chrome('chromedriver.exe')

	def login(self):
		self.driver.get(self.login_url)
		print('got to insta\n')

		time.sleep(2)







if __name__=='__main__':
	ig_bot = Instagramb('george', 'temppass')

	ig_bot.login()