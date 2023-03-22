from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
PATH = r'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(service=Service(PATH))
driver.get("https://techwithtim.net")

search = driver.find_element_by_name('q')
search.send_keys('test')
search.send_keys(Keys.RETURN)


