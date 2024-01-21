from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://www.youtube.com/@somoynews360/videos')
driver.get('https://www.google.com/maps/search/United+States+new+york+restorant/@40.7416519,-74.0232842,14z/data=!4m2!2m1!6e5?entry=ttu')

time.sleep(30)

link_list = []
name = []

for i in range(1,141):
    #driver.execute_script("window.scrollTo(0, -1080)") 
    driver.execute_script("scrollBy(0, 768);")
    
    # print(i)
    try:
        elems = driver.find_element(By.XPATH, value = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div['+str(i)+']/div/a')
        print(elems.get_attribute("href"))
        link_list.append(elems.get_attribute("href"))
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        name.append(elems.text)
    except:
        print("error")

    try:
        elems = driver.find_element(By.XPATH, value = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row['+str(i)+']/div/ytd-rich-item-renderer[2]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a')
        print(elems.get_attribute("href"))
        link_list.append(elems.get_attribute("href"))
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        name.append(elems.text)
    except:
        print("error")

    try:
        elems = driver.find_element(By.XPATH, value = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row['+str(i)+']/div/ytd-rich-item-renderer[3]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a')
        print(elems.get_attribute("href"))
        link_list.append(elems.get_attribute("href"))
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        name.append(elems.text)
    except:
        print("error")

    try:
        elems = driver.find_element(By.XPATH, value = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row['+str(i)+']/div/ytd-rich-item-renderer[4]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a')
        print(elems.get_attribute("href"))
        link_list.append(elems.get_attribute("href"))
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        name.append(elems.text)
    except:
        print("error")
    print(str(i))       


print(i)
print(link_list)


final_dicts = (list(zip(link_list,name )))
import pandas as pd
df = pd.DataFrame(final_dicts)
print(df)

header_list = ['Company_Name','Address','City','State','Zip_code','Phone_Numbers','Rating','Reviews','Website','Email',]

df.to_csv('Youtube.csv',index=False, header=header_list)


time.sleep(30)
