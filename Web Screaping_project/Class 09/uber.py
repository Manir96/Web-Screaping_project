from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.daraz.com.bd/televisions/?spm=a2a0e.home.cate_7.1.735212f7TtdkVw')


cat_list= []

for i in range(1,40):
    k = str(i)

    category = driver.find_element(by=By.XPATH, value = '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[5]/div/div/div['+k+']/div/a/img')
    cat_list.append(category.text)

print(cat_list)
print(len(cat_list)) 
time.sleep(50)