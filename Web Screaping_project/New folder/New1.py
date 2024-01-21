from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))#
#driver.get("https://www.daraz.com.bd/mens-t-shirts/?page=1&spm=a2a0e.home.cate_4_1.1.fee312f7sCPKy2")

title_list = [] 
dicts = {}
price_list = []
original_price_list = []
rat = []
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
for j in range(0,100):
    # driver.get('https://www.daraz.com.bd/mens-sports-watches/?page='+str(j)+'&spm=a2a0e.searchlistcategory.cate_4_7.4.784f2819i1EZoQ')
    driver.get('https://www.google.com/maps/search/United+States+new+york+restorant/@40.7225657,-74.0220915,14z/data=!3m1!4b1?entry=ttu')
    
    for i in range(1,150):
        try:           
            # x = str(i)
        
            title = driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/h1')
        
            title_list.append(title.text)
        except:
            title_list.append("none")           
    for i in range(1,41):
        try: 
            # x = str(i)
        
            price = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[3]/span')
        
            price_list.append(price.text)
        except:
            price_list.append("৳0")
    for i in range(1,41):    
        try:    
        
            original_price = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[4]/span[1]/del')
        
            original_price_list.append(original_price.text)
        except:
            original_price_list.append("৳0")
    for i in range(1,41):    
        try:    
        
            rating=driver.find_element(by=By.XPATH, value = '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[5]/div/span[6]')
        
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



#import pandas as pd
#Choice = input ('Is product dict have catagory as key? type : "y" , "n". If it is ony as list type : "0" ')
#Catagory = ['Picked for you', 'Featured', 'Ultimate Drink Stop', 'Burgers', 'Chicken', 'Hot Dogs', "Kids' Meals", 'All Day Breakfast', 'Snacks & Sides', 'Frozen Zone', 'Everyday Deals']
#Product = {'Picked for you': [['SONIC� Cheeseburger', 'Chili Cheese Coney', 'Sausage Breakfast Burrito', 'SuperSONIC� Double Cheeseburger', 'Hot Fudge Sundae'], ['BDT 5.72', 'BDT 3.65', 'BDT 4.87', 'BDT 7.80', 'BDT 3.28']], 'Featured': [['Broccoli Cheddar Tots', 'Steak Butter Bacon Cheeseburger', 'Regular FRITOS� Chili Cheese Wrap'], ['Priced by add-ons', 'BDT 6.58', 'BDT 3.65']], 'Ultimate Drink Stop': [['Famous Slushes', 'Real Fruit Slushes', 'Limeades and Lemonades', 'Soft Drinks', 'Water', 'Iced Tea', 'Original Cold Brew Iced Coffee', 'French Vanilla Cold Brew Iced Coffee', 'Green Mountain Coffee Roasters� Coffee', 'Minute Maid� 100% Apple Juice Box', 'Milk Jug (1%) - White', 'Cup of SONIC� Ice'], ['Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'BDT 2.43', 'BDT 2.06', 'BDT 1.82', 'Priced by add-ons']], 'Burgers': [['SONIC� Cheeseburger', 'Quarter Pound Double Cheeseburger', 'SuperSONIC� Double Cheeseburger', 'SuperSONIC� Bacon Double Cheeseburger', 'Plain SONIC Cheeseburger', 'Steak Butter Bacon Cheeseburger'], ['BDT 5.72', 'BDT 3.65', 'BDT 7.80', 'BDT 8.53', 'BDT 5.72', 'BDT 6.58']], 'Chicken': [['Jumbo Popcorn Chicken�', 'Buffalo Sauced Jumbo Popcorn Chicken�', 'Honey BBQ Sauced Jumbo Popcorn Chicken�', 'Crispy Tenders Dinner', 'Crispy Chicken Tenders', 'Classic Crispy Chicken Sandwich'], ['Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'BDT 7.31']], 'Hot Dogs': [['Chili Cheese Coney', 'All-American Dog', 'Footlong Quarter Pound Coney', 'Corn Dog'], ['BDT 3.65', 'BDT 3.65', 'BDT 6.09', 'BDT 2.31']], "Kids' Meals": [['Wacky Pack� Jr Burger', 'Wacky Pack� Chicken Strips', 'Wacky Pack� 100% Beef Hot Dog', 'Wacky Pack� Corn Dog', 'Wacky Pack� Grill Cheese Sandwich'], ['Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons']], 'All Day Breakfast': [['Bacon Breakfast TOASTER�', 'Sausage Breakfast TOASTER�', 'Bacon Breakfast Burrito', 'Sausage Breakfast Burrito', 'Ultimate Meat & Cheese Breakfast Burrito�', 'SuperSONIC� Breakfast Burrito', 'Jr. Sausage, Egg and Cheese Breakfast Burrito', 'Jr. Bacon, Egg and Cheese Breakfast Burrito', 'Cinnabon� Cinnasnacks� with Cream Cheese Frosting', 'Green Mountain Coffee Roasters� Coffee', 'French Vanilla Cold Brew Iced Coffee', 'Original Cold Brew Iced Coffee'], ['BDT 5.48', 'BDT 5.48', 'BDT 4.87', 'BDT 4.87', 'BDT 6.09', 'BDT 6.09', 'BDT 2.43', 'BDT 2.43', 'Priced by add-ons', 'BDT 2.43', 'Priced by add-ons', 'Priced by add-ons']], 'Snacks & Sides': [['Tots', 'Chili Cheese Tots', 'Cheese Tots', 'Fries', 'Chili Cheese Fries', 'Cheese Fries', 'Ched �R� Peppers�', 'Hand Made Onion Rings', 'Soft Pretzel Twist', 'Jumbo Popcorn Chicken�', 'Buffalo Sauced Jumbo Popcorn Chicken�', 'Honey BBQ Sauced Jumbo Popcorn Chicken�', 'Corn Dog', 'Mozzarella Sticks', 'Broccoli Cheddar Tots', 'Regular FRITOS� Chili Cheese Wrap'], ['Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'BDT 2.43', 'Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'BDT 2.31', 'Priced by add-ons', 'Priced by add-ons', 'BDT 3.65']], 'Frozen Zone': [['SONIC Blasts�', 'Hand-Mixed Master Shakes', 'Hand-Mixed Classic Shakes', 'Hot Fudge Sundae'], ['Priced by add-ons', 'Priced by add-ons', 'Priced by add-ons', 'BDT 3.28']], 'Everyday Deals': [['Quarter Pound Double Cheeseburger', 'Grilled Cheese', 'Jr. Sausage, Egg and Cheese Breakfast Burrito', 'Jr. Bacon, Egg and Cheese Breakfast Burrito'], ['BDT 3.65', 'BDT 2.67', 'BDT 2.43', 'BDT 2.43']]}


header_list = ['Product','Present Price','Original_price','Rating']

#if Choice == "n" :

#final_catagory_product_dict = (zip(title,list(Product.values())))

#df = pd.DataFrame(list(final_catagory_product_dict))
#print(df)
df.to_csv('mmens-sports-watches.csv',index=False, header=header_list)


time.sleep(50)