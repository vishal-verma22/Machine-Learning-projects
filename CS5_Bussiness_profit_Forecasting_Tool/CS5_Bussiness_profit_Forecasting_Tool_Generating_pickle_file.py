"""
=>Creating Bussiness Profit Forecasting Tool
=>Using Multilinear Regression
=>Using Tkniter for GUI
=>Generating Pickle file
"""

# import library

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pickle import dump
# load the data

data=pd.read_csv("cs5_jan26.csv")
print(data)

#Checking for missing value 

print("Checking missing value\n",data.isnull().sum())

#feature & target
features=data[["R&D Spend","Administration","Marketing Spend"]]
target=data["Profit"]

#train & test

x_train,x_test,y_train,y_test=train_test_split(features,target)

#model

model=LinearRegression()
model.fit(x_train,y_train)

#performance

train_score=model.score(x_train,y_train)
print("model score",train_score)

#pickle file

f=open("Generating_pikl_of_cs5.pkl","wb")
dump(model,f)
f.close()
print("Pickle File Created Successfully")
