"""
Lonavala House Price Predictor using ML & Tkinter
"""

# =======================
#	 ML
# =======================


#import the library

import matplotlib.pyplot as plt
from tkinter import *
import pandas as pd
from sklearn.linear_model import LinearRegression


# Load Data

data = pd.read_csv("cs1_jan26.csv")

#fearure and target

feature = data[["area in square feet"]]
target = data["price (in crores)"]

#model

model = LinearRegression()
model.fit(feature, target)

#Graph of dataset

plt.figure(figsize=(11,5))
plt.title("Area vs Price ")
plt.scatter(feature,target,color="red",s=100)
plt.plot(feature,model.predict(feature),label="Regression Line")
plt.xlabel("Price")
plt.ylabel("Area")
plt.legend()
plt.show()


# Function to predicat the output

def check_price():
    try:
        area = float(EntryArea.get())
        result = model.predict([[area]])
        price = round(result[0], 2)

        labMsg.config(
            text=f"💰 Estimated Price: ₹ {price} Crores",
            fg="#00ff88"   
        )
    except:
        labMsg.config(
            text="⚠ Please enter valid area!",
            fg="#ff3333"
        )

# =======================
#	 GUI
# =======================

root = Tk()
root.geometry("1000x600+150+100")
root.title("Lonavala House Price Predictor")
root.config(bg="#1e3c72")

labHeading = Label(
    root,
    text="🏠 Lonavala House Price Predictor",
    font=("Segoe UI", 26, "bold"),
    bg="#1e3c72",
    fg="#ffd700"
)

labSubHeading = Label(
    root,
    text="Enter property area in square feet to estimate price",
    font=("Segoe UI", 12, "italic"),
    bg="#1e3c72",
    fg="white"
)

EntryArea = Entry(
    root,
    font=("Segoe UI", 14),
    width=25,
    bd=0,
    justify="center"
)

btnCheck = Button(
    root,
    text=" Predict Price ",
    font=("Segoe UI", 14, "bold"),
    bg="#ff9800",   
    fg="white",
    activebackground="#e68900",
    activeforeground="white",
    bd=0,
    padx=25,
    pady=10,
    command=check_price
)

labMsg = Label(
    root,
    text="",
    font=("Segoe UI", 16, "bold"),
    bg="#1e3c72"
)


labHeading.pack(pady=40)
labSubHeading.pack(pady=5)
EntryArea.pack(pady=20)
btnCheck.pack(pady=20)
labMsg.pack(pady=20)

root.mainloop()
