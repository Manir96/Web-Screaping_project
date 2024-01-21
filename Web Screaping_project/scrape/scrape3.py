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
j = 0
link_list = []

# for elem in elems:
#     print(elem.get_attribute("href"))
#     i=i+1
#     print(i)
#     link_list.append(elem.get_attribute("href"))
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     # time.sleep(2)


total_price = driver.find_element(By.XPATH, value='//*[@id="app"]/section[2]/div/div[3]/div[1]/div/div[1]/div[1]/div/div/a/div/strong/span').text
total_price = total_price.replace("(", "")
total_price = total_price.replace(",", "")
total_price = total_price.replace(")", "")
total_price = int(total_price)
elems = driver.find_element(By.XPATH, value = '//*[@id="app"]/section[2]/div/div[3]/div[1]/div/div[1]/div[1]/div/div/a/div/strong/span')
driver.execute_script("arguments[0].scrollIntoView();", elems)
print(elems.get_attribute("href"))

for i in range(1,total_price+1):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # print(i)
    # try:
    #     elems = driver.find_element(By.XPATH, value = '//*[@id="app"]/section[2]/div/div[3]/div[1]/div/div[1]/div['+str(i)+']/div/a[1]')
    #     print(elems.get_attribute("href"))
    #     link_list.append(elems.get_attribute("href"))
    #     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # except:
    #     print("error")
for i in range(1,total_price+1):
    # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # print(i)
    try:
        elems = driver.find_element(By.XPATH, value = '//*[@id="app"]/section[2]/div/div[3]/div[1]/div/div[1]/div[+str(i)+]/div/div/a/div/strong/span')
        print(elems.get_attribute("href"))
        link_list.append(elems.get_attribute("href"))
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    except:
        print("error")


print(i)
print(link_list)

time.sleep(30)