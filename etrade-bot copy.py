from selenium import webdriver
import pyautogui
import time
import random

class EtradeBot:
	def __init__(self):
		self.userid = (696, 525)
		self.auto_password = (772,604)
		self.loginbutton = (720,724)

		self.username = ''#
		self.password = ''#
		self.browser = webdriver.Chrome()
		self.browser.get('https://us.etrade.com/e/t/user/login')
		time.sleep(1)

	def autologin(self):
		pyautogui.moveTo(self.userid[0], self.userid[1], 2) #take 2seconds to get to  login entry 
		pyautogui.click()
		pyautogui.write(self.username)
		pyautogui.moveTo(self.auto_password[0], self.auto_password[1], 2)
		pyautogui.click()
		pyautogui.write(self.password)
		time.sleep(1)
		pyautogui.moveTo(self.loginbutton[0], self.loginbutton[1], 1)
		pyautogui.click()

	def trade(self, stock):
		self.browser.find_element_by_xpath('//*[@id="new-nav-layout"]/div[3]/div[3]/div[2]/a').click()
		time.sleep(2)
		self.browser.find_element_by_xpath('//*[@id="symbol"]').send_keys(stock)# stock symbl, make it all caps
		pyautogui.press('enter')
		pyautogui.moveTo(88, 574, 2)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(161, 594, 2)
		pyautogui.click()
		pyautogui.moveTo(305, 570, 2)
		pyautogui.click()
		pyautogui.write('1') #number of stocks to buy
		pyautogui.moveTo(143, 636, 2)
		pyautogui.click()
		pyautogui.moveTo(158, 656, 1)
		pyautogui.click()
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.moveTo(757, 810, 2)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(742, 715, 1)
		pyautogui.click()
		time.sleep(3)


bot = EtradeBot()
bot.autologin()
time.sleep(4)
bot.trade('LUV')
bot.browser.quit()
