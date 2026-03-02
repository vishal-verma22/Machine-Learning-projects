"""
=>Salary Predictor System based on Experience
=>Using LinearRegression Model
=>Handling missing data
=>Tkinter for GUI Deveploment
"""

#=================
# 	ML
#=================

#import library

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import*

#load the data

data=pd.read_csv("cs4_jan26.csv")
print(data)
print(data.shape)


#checking missing value in dataset

print(data.isnull().sum())

#checking skewness of data

print(data.skew())

sns.histplot(data["Experience (years)"],kde=True)
plt.show()

sns.histplot(data["Salary (thousands of dollars)"],kde=True)
plt.show()


#filling missing value

data["Experience (years)"]=data["Experience (years)"].fillna(data["Experience (years)"].mean())
data["Salary (thousands of dollars)"]=data["Salary (thousands of dollars)"].fillna(data["Salary (thousands of dollars)"].median())

print(data.isnull().sum())

#feature & target

feature=data[["Experience (years)"]]
target=data["Salary (thousands of dollars)"]

#splitting the data into train & test

x_train,x_test,y_train,y_test=train_test_split(feature,target)

#model

model=LinearRegression()
model.fit(x_train,y_train)

#performance score

train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print(train_score)
print(test_score)




#graph
"""
plt.figure(figsize=(12,5))
plt.scatter(feature, target, color='blue', label="Actual Data Point")

plt.plot(feature, model.predict(feature), color='red', label="Regression Line")

plt.xlabel("Experience (years)")
plt.ylabel("Salary (thousands of dollars)")
plt.title("Salary vs Experience")
plt.legend()
plt.show()
plt.show()

"""

#=================
# 	GUI
#=================
def check_salary():
	experience=labEntry.get()
	
	if experience=="":
		labMsg.config(text="Please Enter the Experience")
		return

	try:
		experience=float(experience)
		estimated_salary=model.predict([[experience]])
		labMsg.config(
			text=f"👨‍💼 Experience: {experience} Years\n"
			f"💰 Expected Salary: ${estimated_salary[0] * 1000:,.2f} USD"
			)
	except ValueError:
		labMsg.config(text="Please Enter Number Only")
		return		

root = Tk()
root.title("Salary Predictor")
root.geometry("900x550+200+100")
root.config(bg="#141e30")

card = Frame(
	root,
	bg="white",
	bd=0,
	relief="flat"
)
card.place(relx=0.5, rely=0.45, anchor="center", width=500, height=380)

labHeading = Label(
	card,
	text="💼 Salary Predictor",
	font=("Segoe UI", 28, "bold"),
	bg="white",
	fg="#141e30"
)

labSub = Label(
	card,
	text="Enter Your Experience (Years)",
	font=("Segoe UI", 14),
	bg="white",
	fg="#555555"
)

labEntry = Entry(
	card,
	font=("Segoe UI", 18),
	width=18,
	justify="center",
	bd=2,
	relief="groove"
)

btncheck = Button(
	card,
	text="Predict Salary",
	command=check_salary,
	font=("Segoe UI", 14, "bold"),
	bg="#ff4b2b",
	fg="white",
	activebackground="#ff416c",
	activeforeground="white",
	padx=20,
	pady=8,
	cursor="hand2",
	relief="flat"
)

labMsg = Label(
	root,
	text="",
	font=("Segoe UI", 20, "bold"),
	bg="#141e30",
	fg="#00e676"    
 )



labHeading.pack(pady=25)
labSub.pack(pady=5)
labEntry.pack(pady=15)
btncheck.pack(pady=20)
labMsg.place(relx=0.5, rely=0.90, anchor="center")

root.mainloop()