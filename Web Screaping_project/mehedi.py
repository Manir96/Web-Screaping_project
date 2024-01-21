from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.realtor.com/realestateandhomes-detail/14025-NW-Robinhood-Ln_Kansas-City_MO_64164_M80651-49543')

price_array = [10]
cat_list =[]
price_list =[]
for i in range(0,10):
    k = str(i)

    category = driver.find_element(by=By.XPATH, value='//*[@id="section_summary"]/div[1]/div[1]/span/div/div/div[1]/h2/div/div/div').text
    cat_list.append(category)
    


print(cat_list)
print(len(cat_list))

time.sleep(50)
