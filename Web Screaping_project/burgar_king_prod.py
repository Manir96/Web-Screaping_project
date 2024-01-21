
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.ubereats.com/nl-en/store/burger-king-16-beaver-street/5pINTOFMSz6v0BxQ5K02qw?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzMjkxMyUyQyUyMmxvbmdpdHVkZSUyMiUzQS03NC4wMDcwNzY3JTdE')

prod_title_list =[]
prod_array = [5,18,22,3,2,5,5,4]
l = 0
for i in range(1,9):
    for j in range(1,(prod_array[l]+1)):
        prod_title = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[4]/div[1]/div[4]/ul/li['+str(i)+']/ul/li['+str(j)+']/div/div/div[2]/div[1]/div/span')
        prod_title_list.append(prod_title.text)
        l = l+1
        
    k = str(i)

    

print(prod_title_list)
print(len(prod_title_list))

time.sleep(50)
