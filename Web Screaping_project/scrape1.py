from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.brilliance.com/lab-grown-diamonds')

time.sleep(30)

#shape click

# for i in range(1,11):
#     x_path = driver.find_element(by=By.CSS_SELECTOR, value='#ds-shapes > ul > li:nth-child('+str(i)+') > div.text-center > i')
#     x_path.click()
#     time.sleep(10)
elems = driver.find_elements(By.TAG_NAME, value = "a")
i = 0
link_list = []

for elem in elems:
    print(elem.get_attribute("href"))
    i=i+1
    print(i)
    link_list.append(elem.get_attribute("href"))
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(10)

print(i)
print(link_list)
time.sleep(30)