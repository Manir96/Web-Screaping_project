from selenium import webdriver
import time

# Get the website using the Chrome webbdriver
browser = webdriver.Chrome()
browser.get('https://www.woofshack.com/en/cloud-chaser-waterproof-softshell-dog-jacket-ruffwear-rw-5102.html')

# Print out the result
price = browser.find_element_by_id('product-price-665')
print("Price: " + price.text)

#store it into a data frame for saving to Excel at a later time in the script
import numpy as np
import pandas as pd
df = pd.DataFrame([["woofshack.com", price.text]], columns=["Website","Price"])

# Close the browser
#time.sleep(3)
#browser.close()

#Repeat the step for website no. 2, etc...
browser.get('https://www.bricoinn.com/en/ruffwear-cloud-chaser-jacket/138328147/p')
price = browser.find_element_by_id('datos_producto_precio')
print("Price: " + price.text)


#Put in the product B price into the table
df2 = pd.DataFrame([["bricoinn.com", price.text]], columns=["Website","Price"])
df=df.append(df2, ignore_index=True)

#Repeat the step for website no. 3, etc...
browser.get('https://www.trekkinn.com/outdoor-mountain/ruffwear-cloud-chaser-jacket/138328147/p')
price = browser.find_element_by_id('datos_producto_precio')
print("Price: " + price.text)


#Put in the product C price into the table
df3 = pd.DataFrame([["trekkinn.com", price.text]], columns=["Website","Price"])
df=df.append(df3, ignore_index=True)

print(df)

# Close the browser

browser.close()