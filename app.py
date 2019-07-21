from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class bot:
    def __init__(self,username,password):
        self.bot = webdriver.Firefox()
        self.username = username
        self.password = password    
    def login(self):
        bot = self.bot
        bot.get('https://www.youtube.com/')
        bot.find_element_by_class_name('style-suggestive').click()
        name = bot.find_element_by_name('identifier').send_keys(self.username+Keys.RETURN)
        time.sleep(2)
        password = bot.find_element_by_name('password').send_keys(self.password+Keys.RETURN)
        time.sleep(3)
    def search(self,data):
        bot = self.bot
        self.data = data
        data = bot.find_element_by_name('search_query').send_keys(self.data+Keys.RETURN)
        time.sleep(3)
        bot.find_element_by_id('avatar').click()
        time.sleep(3)
        bot.find_element_by_id('tip').click()
        #sub = bot.find_element_by_class_name('paper-ripple').click()
        
        time.sleep(3)
        bot.quit()
test = bot("twitterbot1966@gmail.com","cobrakill123")
test.login()
test.search('pewdiepie')