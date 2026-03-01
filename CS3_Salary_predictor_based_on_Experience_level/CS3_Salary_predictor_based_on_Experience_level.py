"""
=>Salary Predictor System based on Experience
=>Using LinearRegression Model
=>Tkinter for GUI Deveploment
"""

#=================
#  ML
#=================

#import the library

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from tkinter import*
from tkinter import font

#load the data

data=pd.read_csv("cs3_jan26.csv")
print(data)

#feature & target

feature=data[["exp"]]
target=data["sal"]

#model

model=LinearRegression()
model.fit(feature.values,target)

#graph
plt.figure(figsize=(12,5))
plt.title("Experience vs Salary")
plt.scatter(feature,target,color="red",label=" Actual Data Point")
plt.plot(feature,model.predict(feature),label="Regression Line")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()


#=================
#  GUI
#=================

def check_salary():
	exp = EntryExperience.get()

	if exp == "":
		labMsg.config(text="Please enter experience")
		return
	
	try:
		exp = float(exp)
	except ValueError:
		labMsg.config(text="Please enter numbers only")
		return

	predicted_salary = model.predict([[exp]])

	labMsg.config(text=f"Expected salary of an employee with {exp} years experience is ₹{round(predicted_salary[0], 2)} lakh per annum")




root = Tk()
root.title("Salary Predictor")
root.geometry("800x500+100+100")
root.configure(bg="#f0f4f8")  # soft background color

heading_font = ("Segoe UI", 28, "bold")
label_font = ("Segoe UI", 16)
entry_font = ("Segoe UI", 14)
button_font = ("Segoe UI", 14, "bold")


HeadingLab = Label(root, text="💰 Salary Predictor", font=heading_font, bg="#f0f4f8", fg="#1e3c72")

EntryExperience = Entry(root, font=entry_font, width=20, justify='center', bd=3, relief=RIDGE)

btnCheck = Button(root, text="Check Salary", font=button_font, bg="#1e3c72", fg="white",
                  activebackground="#274b9c", activeforeground="white", padx=20, pady=10,command=check_salary)

labMsg = Label(root, text="", font=label_font, bg="#f0f4f8", fg="#ff4500")


HeadingLab.pack(pady=30)
EntryExperience.pack(pady=20)
btnCheck.pack(pady=20)
labMsg.pack(pady=20)



root.mainloop()