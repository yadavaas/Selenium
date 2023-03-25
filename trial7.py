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
driver.implicitly_wait(10)
driver.get('https://www.naukri.com/data-analyst-jobs?k=data%20analyst')
# driver.maximize_window()
# driver.minimize_window()
data_list = []

sections = driver.find_elements(By.TAG_NAME, 'article')
# sections = driver.find_elements(By.XPATH, '//*[@id="root"]/div[4]/div/div/section[2]/div[2]/article[3]')
print('length of section is: ', len(sections))
# print(sections)

for section in sections:

    company_data = {}


    skills = section.find_element(By.CLASS_NAME, 'tags.has-description').text
    print(skills)

    # company_data['skills'] = skills
    #
    # data_list.append(company_data)





# data_df = pd.DataFrame(data_list)
# # data_df.to_csv('jobDataset.csv')
# print(data_df.skills)

print('done')

# time.sleep(5)
# driver.close()