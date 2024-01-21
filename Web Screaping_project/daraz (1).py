import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
daraz = pd.read_csv(r'D:\Python\Programs\monir_electronics__mobile.csv')

O_price_list= []

for i in daraz['O_price']:
    x = i.split(' ')
#    print(x[1])
    O_price_list.append(x[1])
type(O_price_list)

print(daraz)
print(daraz['O_price'])
daraz['O_price'] = O_price_list
print(daraz)

daraz.to_csv(r'D:\Python\Programs\monir_electronics__mobile.csv')