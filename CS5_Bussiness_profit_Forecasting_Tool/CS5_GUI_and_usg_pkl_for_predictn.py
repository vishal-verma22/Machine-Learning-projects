"""
=> Here we are using the generated pickle file for prediction
"""

from tkinter import *
from pickle import load


# Load Model
with open("Generating_pikl_of_cs5.pkl", "rb") as f:
	model = load(f)


# GUI Function
def Predict_profit():

	rd_spend = R_dEntry.get()
	admn = AdministrationEntry.get()
	marktspnd = MarketingSpendEntry.get()

	if rd_spend == "":
		labMsg.config(text="⚠ Please enter R&D Spend.")
		return

	if admn == "":
		labMsg.config(text="⚠ Please enter Administration cost.")
		return

	if marktspnd == "":
		labMsg.config(text="⚠ Please enter Marketing Spend.")
		return

	try:
		rd_spend = float(rd_spend)
	except ValueError:
		labMsg.config(text=" Enter a valid numeric value for R&D Spend.")
		return

	try:
		admn = float(admn)
	except ValueError:
		labMsg.config(text=" Enter a valid numeric value for Administration.")
		return

	try:
		marktspnd = float(marktspnd)
	except ValueError:
		labMsg.config(text=" Enter a valid numeric value for Marketing Spend.")
		return

	predicted_profit = model.predict([[rd_spend, admn, marktspnd]])
	labMsg.config(text=f"💰 Predicted Profit: ₹ {predicted_profit[0]:,.2f}")



# Main Window
root = Tk()
root.title("🚀 AI Business Profit Predictor")
root.geometry("900x520+100+40")
root.config(bg="#101820")   

# Center Card Frame
card = Frame(root, bg="#1b2a41", bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=460)


# Heading
labHeading = Label(
	card,
	text="📊 Business Profit Forecasting Tool",
	font=("Segoe UI", 20, "bold"),
	bg="#1b2a41",
	fg="#00c2ff"
)


# Labels & Entries
R_dLabel = Label(card, text="🔬 R&D Spend (₹)", font=("Segoe UI", 12, "bold"), bg="#1b2a41", fg="white")
R_dEntry = Entry(card, font=("Segoe UI", 12), width=28, bd=0, bg="#243b55", fg="white", insertbackground="white")

AdministrationLabel = Label(card, text="🏢 Administration Cost (₹)", font=("Segoe UI", 12, "bold"), bg="#1b2a41", fg="white")
AdministrationEntry = Entry(card, font=("Segoe UI", 12), width=28, bd=0, bg="#243b55", fg="white", insertbackground="white")

MarketingLabel = Label(card, text="📢 Marketing Spend (₹)", font=("Segoe UI", 12, "bold"), bg="#1b2a41", fg="white")
MarketingSpendEntry = Entry(card, font=("Segoe UI", 12), width=28, bd=0, bg="#243b55", fg="white", insertbackground="white")



btnpredict = Button(
	card,
	text="✨ Predict Profit",
	font=("Segoe UI", 12, "bold"),
	bg="#00c2ff",
	fg="black",
	width=20,
	bd=0,
	activebackground="#00e5ff",
	command=Predict_profit
)


labMsg = Label(
	card,
	text="",
	font=("Segoe UI", 13, "bold"),
	bg="#1b2a41",
	fg="#7CFC00"
)



labHeading.pack(pady=30)

R_dLabel.pack()
R_dEntry.pack(pady=8)

AdministrationLabel.pack()
AdministrationEntry.pack(pady=8)

MarketingLabel.pack()
MarketingSpendEntry.pack(pady=8)

btnpredict.pack(pady=25)

labMsg.pack(pady=15)


root.mainloop()