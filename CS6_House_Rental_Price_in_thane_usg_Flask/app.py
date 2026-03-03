
#-->import library

from flask import*
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#-->load the data

data=pd.read_csv("cs6_house_rent_feb26.csv")
print(data)

#-->checking missing value

print("Checking missing null value\n",data.isnull().sum())

#-->Converting Categorical value into numbers

encoder=OneHotEncoder()
encoded_category=encoder.fit_transform(data[["furnishing_status"]]).toarray()
columns_name= encoder.get_feature_names_out(["furnishing_status"])

#-->converting into dataframe
converted_categorical_data=pd.DataFrame(encoded_category, columns=columns_name)


#-->combining the Encode columns with old columns

features=pd.concat([data.drop(["rent","furnishing_status"],axis=1),converted_categorical_data],axis=1)
print("features are\n",features)

#target
target=data["rent"]

#-->train & split
x_train,x_test,y_train,y_test=train_test_split(features,target)

#-->model
model=LinearRegression()
model.fit(x_train,y_train)

#-->performance
train_score=model.score(x_train,y_train)
print(train_score)


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def check_price():
	if request.method=="POST":

		bedroom=int(request.form.get("bedroom"))
		area=float(request.form.get("area"))
		furnishing=request.form.get("furnishing")
		bathroom=int(request.form.get("bathroom"))

		if furnishing=="Furnished":
			d=[bedroom,area,bathroom,1,0,0]
		elif furnishing=="Semi-Furnished": 	
			d=[bedroom,area,bathroom,0,1,0]
		elif furnishing=="Unfurnished": 	
			d=[bedroom,area,bathroom,0,0,1]

		df=pd.DataFrame([d])
		estimated_price=model.predict(df)
		
		return render_template("home.html",message=[round(estimated_price[0],2),bedroom,area,furnishing,bathroom])
	else:
		return render_template("home.html")

app.run(debug=True,use_reloader=False)