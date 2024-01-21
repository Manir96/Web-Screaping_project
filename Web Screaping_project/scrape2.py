from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
price_list = []




driver.get('https://www.brilliance.com/lab-grown-diamonds')


for j in range(1,177534):
    for i in range(1,177534):    
        try:    

                price = driver.find_element(by=By.XPATH, value='//*[@id="app"]/section[2]/div/div[3]/div[1]/div/div[1]/div[+str(i)+]/div/div/a/div/strong/span')

                price_list.append(price.text)
        except:
                price_list.append("$1,000")


print(price_list)