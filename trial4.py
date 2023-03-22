from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.naukri.com/data-analyst-jobs?k=data%20analyst')
# driver.maximize_window()
driver.minimize_window()
jobs = []
titles = driver.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "subTitle", " " ))]')
for title in titles:
    jobs.append(title.text)
    print((title.text))

job_df = pd.DataFrame({'company':jobs})
job_df.to_csv('jobDataset.csv')
print('done')
