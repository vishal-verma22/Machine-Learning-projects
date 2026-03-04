"""
=>Creating model that predicat Price of Used car
=>Here we Generating pickle file of model
=>Using MultipleLinearRegression
"""


#import the library

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pickle import dump

#load the data

data=pd.read_csv("cs8_car_price_feb26.csv")
print(data)

#check null data

print("Checking for null data\n",data.isnull().sum())


#column tranformer

categorical_cols=["car_name"]
numeric=["age_years", "kms_driven"]

column_tranformer = ColumnTransformer(
    transformers=[
        ("categorical_column", OneHotEncoder(), ["car_name"]),
        ("numeric", MinMaxScaler(), ["age_years", "kms_driven"])
    ],remainder='passthrough'

)
pipeline=make_pipeline(column_tranformer,LinearRegression())


#feature & target

features=data.drop("price",axis=1)
target=data["price"]

#train & test
x_train,x_test,y_train,y_test=train_test_split(features,target)

#model

pipeline.fit(x_train,y_train)

# Access column transformer
ct = pipeline.named_steps['columntransformer']

# Get transformed column names
column_names = ct.get_feature_names_out()

print(column_names)

name=input("enter name")
age=float(input("Enter age"))
km=float(input("Enter km"))

df=pd.DataFrame([[name,age,km]],columns=["car_name","age_years","kms_driven"])
result=pipeline.predict(df)
print(result)
