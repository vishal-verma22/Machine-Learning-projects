"""
=>Here we Creating Model of LogisticRegression for diabetes classifier 
=>Generating pickle file 
"""

#import the library

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from pickle import dump

#load the data

data=pd.read_csv("cs7_diabetes_feb26.csv")
print(data)

#checking for Null/Missing Value

print("Checking for Null/Missing Value\n",data.isnull().sum())
print("Checking dataset is balanced or not\n",data["Diabetes"].value_counts())  #checking dataset is balanced or not
#checking sknewness

print("skewness \n",data["Fasting_Sugar"].skew())
print("skewness \n",data["HbA1c"].skew())

#graph of skewness
'''
sns.histplot(data["Fasting_Sugar"],kde=True)
plt.show()
sns.histplot(data["HbA1c"],kde=True)
plt.show()
'''
#filling missing value
data["Fasting_Sugar"]=data["Fasting_Sugar"].fillna(data["Fasting_Sugar"].mean())
data["HbA1c"]=data["HbA1c"].fillna(data["HbA1c"].mean())

print("After filling Null/Missing Value\n",data.isnull().sum())

#handling categorical data

encoder=OneHotEncoder()
encoded_data=encoder.fit_transform(data[["Gender","Hypertension","Family_History"]]).toarray()
columns_name=encoder.get_feature_names_out(["Gender","Hypertension","Family_History"])

#making DF

new_df=pd.DataFrame(encoded_data,columns=columns_name)

#combing new-df & old columns

features=pd.concat([data.drop(["Gender","Hypertension","Family_History","Diabetes"],axis=1),new_df],axis=1)
print("feature\n",features)

target=data["Diabetes"]

#train & split

x_train,x_test,y_train,y_test=train_test_split(features,target)
#model

model=LogisticRegression(max_iter=500)
model.fit(x_train,y_train)

#performance

cr=classification_report(y_test,model.predict(x_test))
print(cr)

#Generating pickle file

with open("Generated_pickle_file.pkl","wb") as f:
	dump(model,f)
	print("Model saved")





