"""
=>Here we creating a House predicting model of different town like Lonavala,karjat,khandala
=>Gui using Tkniter

"""

#===================
#	ML
#===================


#import the library

import pandas as pd
from sklearn.linear_model import LinearRegression
from tkinter import*

#load the data

data=pd.read_csv("cs2_jan26.csv")
print(data)

#checking for missing value

print(data.isnull().sum())

#feature and target

features=data[["place","area"]]
target=data["price"]

#handling categorical data

new_features=pd.get_dummies(features)

#model

model=LinearRegression()
model.fit(new_features.values,target)


#===================
#	GUI
#===================



def predict_price():
	area=EntryArea.get()
	location=place_var.get()

#validation

	if area=="":	
		labMsg.config(text="please Enter Area")
		return
	try:
		area=float(area)
		
	except ValueError:
		labMsg.config(text="Please enter a valid number")
		return



		
	if location=="Lonavala":
		l=[area,False,False,True]
	
	elif location=="Khandala":
		l=[area,False,True,False]

	elif location=="Karjat":
		l=[area,True,False,False]
	else:
		labMsg.config(text="please select correct loaction")
		return  



	Estimated_price=model.predict([l])
	labMsg.config(text=f"Estimated Price: ₹{round(Estimated_price[0], 3)} Crores")

root = Tk()
root.geometry("800x500+100+50")
root.title("House Price Predictor")
root.config(bg="#f2f2f2")

heading_font = ("Segoe UI", 26, "bold")
entry_font = ("Segoe UI", 14)
button_font = ("Segoe UI", 14, "bold")
info_font = ("Segoe UI", 12, "italic")

labInfo = Label(root, text="Predict house prices for Lonavala, Khandala & Karjat!", 
                font=info_font, fg="#333333", bg="#d9d9d9")
labHeading = Label(root, text="🏠 House Price Predictor", font=heading_font, fg="#222222", bg="#f2f2f2")
EntryArea = Entry(root, font=entry_font, bd=3, relief=RIDGE, justify=CENTER)


# Variable to store selected value
place_var = StringVar()
place_var.set("Select Place")

# Dropdown menu
places = ["Lonavala", "Khandala", "Karjat"]
dropdown = OptionMenu(root, place_var, *places)
dropdown.config(font=entry_font, width=15, bd=3, relief=RIDGE)

btnPredict = Button(root, text="Predict Price", font=button_font, bg="#4da6ff", fg="white",
                    activebackground="#3399ff", activeforeground="white",command=predict_price)
labMsg = Label(root, text="", font=("Segoe UI", 16, "bold"), fg="#00aa00", bg="#f2f2f2")

labInfo.pack(fill=X, pady=(0,20))
labHeading.pack(pady=10)
EntryArea.pack(pady=10, ipady=5, ipadx=5)
dropdown.pack(pady=10)
btnPredict.pack(pady=20, ipadx=10, ipady=5)
labMsg.pack(pady=20)

root.mainloop()