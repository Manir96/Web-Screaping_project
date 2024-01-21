
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service('C'))


driver.get('https://www.ubereats.com/nl-en/store/juice-press-83-murray-street/nOPAbCyyQO-exPye96mi5g?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzMjkxMyUyQyUyMmxvbmdpdHVkZSUyMiUzQS03NC4wMDcwNzY3JTdE')

cat_list =[]
for i in range(1,15):
    k = str(i)

    category = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[4]/div[1]/div[4]/ul/li['+k+']/div[1]').text
    cat_list.append(category.text)

print(cat_list)
print(len(cat_list))

time.sleep(50)
