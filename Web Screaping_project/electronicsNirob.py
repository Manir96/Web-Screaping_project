from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
cat_list= []
title_list = [] 
dicts = {}
price_list = []
original_price_list = []
rat = []

for j in range(1,103):
    driver.get('https://www.daraz.com.bd/televisions/?spm=a'+str(j)+'a0e.home.cate_7.1.6b8712f7NjewJZ')

    for i in range(1,41):
        try:           
            # x = str(i)

                title = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[2]/a')

                title_list.append(title.text)
        except:
                title_list.append("none")           
    for i in range(1,41):
        try: 
                # x = str(i)

                price = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[4]/span[1]/del')

                price_list.append(price.text)
        except:
                price_list.append("৳0")
    for i in range(1,41):    
        try:    

                original_price = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[3]/span')

                original_price_list.append(original_price.text)
        except:
                original_price_list.append("৳0")
    for i in range(1,41):    
        try:    

                rating=driver.find_element(by=By.XPATH, value = '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[5]/div')

                rat.append(rating.text)   
        except:
                rat.append("0")  


print(title_list)
print(price_list)
print(original_price_list)
print(rat.append)

final_dicts = (list(zip(title_list,price_list,original_price_list,rat)))
import pandas as pd
df = pd.DataFrame(final_dicts)
print(df)


header_list = ['Product','Present Price','Original_price','Rating']

#if Choice == "n" :

#final_catagory_product_dict = (zip(title,list(Product.values())))

#df = pd.DataFrame(list(final_catagory_product_dict))
#print(df)  
df.to_csv('monir_electronics__tv.csv',index=False, header=header_list)


time.sleep(50)