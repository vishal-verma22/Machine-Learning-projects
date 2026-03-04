
from flask import*
import pandas as pd
from pickle import load

with open("Generated_pickle_file.pkl","rb") as f:
	model=load(f)

app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def check_price():

	if request.method=="POST":
	
		car_name=request.form.get("car_name")
		age=float(request.form.get("age_years"))
		kms_driven=float(request.form.get("kms_driven"))
		df=pd.DataFrame([[car_name,age,kms_driven]],columns=["car_name","age_years","kms_driven"])
		result=model.predict(df)
		return render_template("home.html",message=result[0])
	else:
		return render_template("home.html")

		
app.run(debug=True)
