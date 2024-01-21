from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://www.youtube.com/results?search_query=somoy+tv+youtube')

time.sleep(30)

#shape click

# for i in range(1,11):
#     x_path = driver.find_element(by=By.CSS_SELECTOR, value='#ds-shapes > ul > li:nth-child('+str(i)+') > div.text-center > i')
#     x_path.click()
#     time.sleep(10)
elems = driver.find_elements(By.TAG_NAME, value = "a")
i = 0
link_list = []
dicts = {}

for j in range(0,2000):
    driver.get('https://www.youtube.com/@somoynews360')
    
    for i in range(0,40):
        try:           
            # x = str(i)
        
            link = driver.find_element(by=By.XPATH, value='https://youtube.com/shorts/-ncJNFeoMaE?feature=2000')
        
            link_list.append(link.text)
        except:
            link_list.append("none") 

print(i)
print(link_list)
time.sleep(30)

final_dicts = (list(zip(link_list)))
import pandas as pd
df = pd.DataFrame(final_dicts)
print(df)
link_list = ['link_list']

df.to_csv('link_list.csv',index=False, link=link_list)