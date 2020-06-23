import os
import time
import configparser
from utility_methods.utility_methods import *
from selenium import webdriver



class InstagramBot:



	"""

	Initializes an instance of the InstagramBot class. Calls login function to authenticate user

	Args:
		username:str: instagram username, if not specified, read from config
		password:str: instagram password, if not specified, read from config

	Attributes:
		login_url:str: URL for instagram
		nav_user_url:str: URL for a users instagram page
		get_tag_url:str: URL to search for hashtag on instagram
		driver:Selenium.webdriver.Chrome: Chromedriver used to automate browser actions

	"""
	def __init__(self, username=None, password=None):
		self.username = config['IG_AUTH']['USERNAME']
		self.password = config['IG_AUTH']['PASSWORD']

		self.login_url = config['IG_URLS']['LOGIN']
		self.nav_user_url = config['IG_URLS']['NAV_USER']
		self.get_tag_url = config['IG_URLS']['SEARCH_TAGS']

		self.driver = webdriver.Chrome('chromedriver.exe')




	"""

	Logs in via web portal

	
	"""
	def login(self):
		self.driver.get(self.login_url), time.sleep(2)

		self.driver.find_element_by_name('username').send_keys(self.username)
		self.driver.find_element_by_name('password').send_keys(self.password)
		login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
		login_button.click(), time.sleep(2)

		try:
			# 'Not Now' button
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()	
		except:
			pass
		try:
			#'Not Now' button to turning on notifications
			self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
		except:
			pass




	"""

	Navigates to a user's instagram page

	Args:
		user:str: instagram username
	
	"""
	def nav_user(self, user):
		time.sleep(1)
		self.driver.get('{}/{}/'.format(self.nav_user_url, user))




	"""
	Follows a user's instagram page

	Args:
		user:str: instagram uesrname

	"""
	def follow_user(self, user):
		self.nav_user(user), time.sleep(1)

		try:
			followbutton = self.find_buttons('Follow')
			followbutton.click()
			print('followed')
		except:
			print("can't follow")
			pass
	


	
	"""
	Unfollows a user's instagram page

	Args:
		user:str: instagram username
	
	"""
	def unfollow_user(self, user):
		self.nav_user(user), time.sleep(1)

		try:
			buttons = self.driver.find_elements_by_tag_name('Button')[1]
			buttons.click(), time.sleep(1)

			unfollow_button = self.find_buttons('Unfollow')
			unfollow_button.click()
			print('Unfollowed')
		except:
			print('Failed to Unfollow')
			pass



	def find_buttons(self, button_text):
		buttons = self.driver.find_element_by_xpath("//*[text()='{}']".format(button_text))
		return buttons
	
	def track_followers(self):
		if self.button


if __name__ == '__main__':

	# config_file_path = 'config_.ini'
	# config = init_config(config_file_path)

	config = configparser.ConfigParser()
	config.read('config_.ini')


	#creating instance of class
	ig_bot = InstagramBot()
	ig_bot.login()
	# ig_bot.follow_user('mkbhd')
	ig_bot.unfollow_user('mkbhd')


