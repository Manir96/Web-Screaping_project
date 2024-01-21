from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.ubereats.com/store/jamba-juice-2300-16th-st-%23245/pVn8Ov51RjySfJvL-fgdOg?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlRoZSUyMFBpenphJTIwQm95JTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyQ2hJSlc1Y29LZ2I3X1RrUnJWWm5BaWFVbTFBJTIyJTJDJTIycmVmZXJlbmNlVHlwZSUyMiUzQSUyMmdvb2dsZV9wbGFjZXMlMjIlMkMlMjJsYXRpdHVkZSUyMiUzQTI0LjI1ODA2NDclMkMlMjJsb25naXR1ZGUlMjIlM0E4OS45MTYzMzY1JTdE')

prod_title_list= []

prod_array = [7,5,6,3,2,1,4,2,7,5]
l = 0
row = 0
cat_dicts = {}
for i in range(1,11):
    temp_list = []
    for j in range(1,prod_array[l]+1): 
        prod_title = driver.find_element(by=By.XPATH, value = '//*[@id="main-content"]/div[4]/div[1]/div[4]/ul/li['+str(i)+']/ul/li['+str(j)+']/div/div/div[2]/div[1]/div/span')
        prod_title_list.append(prod_title.text)
        temp_list.append(prod_title.text)
    cat_dicts[i-1] = temp_list
    
    l= l+1
   
print(prod_title_list)
print(len(prod_title_list)) 
print(cat_dicts)
time.sleep(50)