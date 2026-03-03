from flask import*
from pickle import*


with open("Generated_pickle_file.pkl","rb") as f:
	model=load(f)

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def check_diabetes():
	if request.method=="POST":
		age=float(request.form.get("age"))
		bmi=float(request.form.get("bmi"))
		fasting_sugar=float(request.form.get("fasting_sugar"))
		hba1c=float(request.form.get("hba1c"))
		gender=request.form.get("gender")
		hypertension=request.form.get("hypertension")
		family_history=request.form.get("family_history")

		
		if gender=="Male":
			g=[0,1]	
		else:
			g=[1,0]

		if hypertension=="Yes":
			h=[0,1]	
		else:
			h=[1,0]

		if family_history=="Yes":
			f=[0,1]	
		else:
			f=[1,0]
		
		d=[age,bmi,fasting_sugar,hba1c]
		d1=[d+g+h+f]
		print(d1)
		result=model.predict(d1)
		print(result[0])
		return render_template("home.html",message=result[0])

	else:				
		return render_template("home.html")



app.run(debug=True)