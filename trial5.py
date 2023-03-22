from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.naukri.com/data-analyst-jobs?k=data%20analyst')
# driver.maximize_window()
driver.minimize_window()
data_list = []
# driver.implicitly_wait(5)
sections = driver.find_elements(By.TAG_NAME, 'article')
print('length of section is: ', len(sections))

time.sleep(5)

for section in sections:

    company_data = {}
    try:
        job_title = section.find_element(By.CLASS_NAME, 'title.ellipsis').text
    except:
        job_title = 'Data Analyst'
    try:
        company = section.find_element(By.CLASS_NAME, 'subTitle.ellipsis.fleft').text
    except:
        company = 'Unknown'
    try:
        salary = section.find_element(By.CLASS_NAME, 'fleft.br2.placeHolderLi.salary').text
    except:
        salary = 'Not disclosed'
    try:
        skills = section.find_elements(By.CLASS_NAME, 'tags.has-description').text
    except:
        skills = 'Not mentioned'
    try:
        job_description = section.find_element(By.CLASS_NAME, 'ellipsis.job-description').text
    except:
        job_description = ''
    try:
        postedDate = section.find_element(By.CLASS_NAME, 'fleft.postedDate').text
    except:
        postedDate = ''
    try:
        url = section.find_element(By.CLASS_NAME, 'title.ellipsis').get_attribute('href')
    except:
        url = ''
    try:
        location = section.find_element(By.CLASS_NAME, 'ellipsis.fleft.locWdth').text
    except:
        location = section.find_element(By.CLASS_NAME, 'ellipsis.fleft.locWdth2').text
    try:
        experience = section.find_element(By.CLASS_NAME, 'ellipsis.fleft.expwdth').text
    except:
        experience = 'not mentioned'
    try:
        rating = section.find_element(By.CLASS_NAME, 'starRating.fleft').text
        reviews = section.find_element(By.CLASS_NAME, 'reviewsCount.fleft').text
    except:
        rating = ''
        reviews = ''

    company_data['job_title'] = job_title
    company_data['company'] = company
    company_data['salary'] = salary
    company_data['experience'] = experience
    company_data['location'] = location
    company_data['skills'] = skills
    company_data['job_description'] = job_description
    company_data['postedDate'] = postedDate
    company_data['rating'] = rating
    company_data['reviews'] = reviews
    company_data['url'] = url

    data_list.append(company_data)





data_df = pd.DataFrame(data_list)
data_df.to_csv('jobDataset.csv')
print(data_df)

print('done')
# driver.close()