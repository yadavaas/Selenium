from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)
# driver.get('https://stackoverflow.com/questions/25829719/why-my-scrapy-response-body-is-empty')
options = Options()
driver = webdriver.Chrome(service=Service(r'C:\Program Files (x86)\chromedriver.exe'))
# driver = webdriver.Chrome(service=Service(PATH,))
driver.get("https://www.google.com")
# print(driver.page_source)

