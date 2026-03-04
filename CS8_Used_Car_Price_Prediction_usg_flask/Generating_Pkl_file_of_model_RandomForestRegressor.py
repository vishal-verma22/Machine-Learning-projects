
#import the library

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from pickle import dump

#load the data

data=pd.read_csv("cs8_car_price_feb26.csv")
print(data)

#check null data

print("Checking for null data\n",data.isnull().sum())


#column tranformer

categorical_cols=["car_name"]

column_tranformer = ColumnTransformer(
    transformers=[
        ("categorical_column", OneHotEncoder(), ["car_name"])
    ],remainder='passthrough'
)
pipeline=make_pipeline(column_tranformer,RandomForestRegressor())


#feature & target

features=data.drop("price",axis=1)
target=data["price"]

#train & test
x_train,x_test,y_train,y_test=train_test_split(features,target)

#model

pipeline.fit(x_train,y_train)

#Generating Pickel file

with open("Generated_pickle_file.pkl","wb") as file:
	dump(pipeline,file)
	
print("model saved successfully")




