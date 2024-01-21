from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.ubereats.com/store/mcdonalds-fillmore/P21H_Lf3Se2wSmjGHfoFcQ?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlRoZSUyMFBpenphJTIwQm95JTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyQ2hJSlc1Y29LZ2I3X1RrUnJWWm5BaWFVbTFBJTIyJTJDJTIycmVmZXJlbmNlVHlwZSUyMiUzQSUyMmdvb2dsZV9wbGFjZXMlMjIlMkMlMjJsYXRpdHVkZSUyMiUzQTI0LjI1ODA2NDclMkMlMjJsb25naXR1ZGUlMjIlM0E4OS45MTYzMzY1JTdE')


cat_list= []

for i in range(1,14):
    k = str(i)

    category = driver.find_element(by=By.XPATH, value = '//*[@id="main-content"]/div[4]/div[2]/div[4]/ul/li['+k+']/div[1]')
    cat_list.append(category.text)

print(cat_list)
print(len(cat_list)) 
time.sleep(50)