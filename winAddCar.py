import tkinter as tk
from tkinter import ttk
import validatingInputs
import communMethods
from car import clsCar
from carCategory import clsCarCategory
from tkinter import messagebox
from decimal import Decimal


import loginInfo

class clsWinAddCar:
	emptyCategor = clsCarCategory.EmptyCarCategoryObject(loginInfo.DB_Mang)

	def __init__(self) :
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add car")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)
		self.window.grab_set()


		Label1 = tk.Label(self.window, text="ADDING NEW CAR", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		

		Labelid = tk.Label(self.window, text="Car id:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Labelid.place(relx=0.15, rely=0.24)
		self.enID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.insert(0, communMethods.generatID_ByDate())
		self.enID.config(state='readonly')
		self.enID.place(relx=0.15, rely=0.3,relheight=0.05)


		Label2 = tk.Label(self.window, text="Make:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2.place(relx=0.4, rely=0.24)
		self.enMake = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enMake.place(relx=0.4, rely=0.3,  relheight=0.05)

		Label3 = tk.Label(self.window, text="Model:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.65, rely=0.24)
		self.enModel = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enModel.place(relx=0.65, rely=0.3,  relheight=0.05)
		 
		Label4 = tk.Label(self.window, text="year:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label4.place(relx=0.15, rely=0.4)
		self.enYear = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enYear.place(relx=0.15, rely=0.46,  relheight=0.05)
		

		Label5 = tk.Label(self.window, text="Milage:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.4, rely=0.4)
		self.enMilage = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enMilage.place(relx=0.4, rely=0.46,  relheight=0.05)

		Label6 = tk.Label(self.window, text="Plate number:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label6.place(relx=0.65, rely=0.4)
		self.enPlateNumber = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enPlateNumber.place(relx=0.65, rely=0.46,  relheight=0.05)
		 
		Label7 = tk.Label(self.window, text="Category:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label7.place(relx=0.15, rely=0.56 )
		self.catsInfo =clsWinAddCar.emptyCategor.getAllCategorysNamesFromTable()
		self.catNames = [t[0] for t in self.catsInfo]
		self.cbCategory = ttk.Combobox(self.window, values=self.catNames, state="readonly")
		self.cbCategory.place(relx=0.15, rely=0.62,  relheight=0.05 )
		self.cbCategory.set(self.catNames[0])
		 
		Label8 = tk.Label(self.window, text="Rantel Price (day):", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label8.place(relx=0.4, rely=0.56 )
		self.enPriceDay = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enPriceDay.place(relx=0.4, rely=0.62,  relheight=0.05)

		Label9 = tk.Label(self.window, text="is available:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label9.place(relx=0.65, rely=0.56 )
		self.cbIsAvail = ttk.Combobox(self.window, values=("yes","no"), state="readonly")
		self.cbIsAvail.set("no")
		self.cbIsAvail.place(relx=0.65, rely=0.62,  relheight=0.05)
		
		 
		self.btnAddCar = tk.Button(self.window, text="ADD", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.addCarToDBtable)
		self.btnAddCar.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()
	def addCarToDBtable(self):
		try:
			id = self.enID.get().strip()
			make = self.enMake.get().strip()
			model = self.enModel.get().strip()
			year = self.enYear.get().strip()
			milage =self.enMilage.get().strip()
			plateNumber = self.enPlateNumber.get().strip()
			CategoryInfo = clsWinAddCar.emptyCategor.searchCategoryInfoInTableByName(self.cbCategory.get())
			carCategoryID = CategoryInfo.categoryID
			if carCategoryID is None:
				raise ValueError("Invalid category")

			rntlPriceDay = self.enPriceDay.get().strip()
			isAvailableForRent = 1 if self.cbIsAvail.get() == "yes" else 0
			
			isValid = validatingInputs.validateCarInputs(id,make, model, year, milage, plateNumber , rntlPriceDay)
			if isValid == True:
			
				self.window.destroy()
				car = clsCar(int(id),make, model, int(year), int(milage), plateNumber, carCategoryID, Decimal(rntlPriceDay), isAvailableForRent,loginInfo.DB_Mang) 

				if car.addCarInfoToDB():
					messagebox.showinfo("Success", "Car added successfully")
				else:
					messagebox.showerror("Error", "Failed to add car")
			else :
				messagebox.showerror("Error", isValid)


		except ValueError as e: 
			messagebox.showerror("error","Invalid Input" )
	# def addCarToDBtable(self):
	# 	try:
	# 		id = int(self.enID.get())
	# 		make = self.enMake.get()
	# 		model = self.enModel.get()
	# 		year = int(self.enYear.get())
	# 		milage = int(self.enMilage.get())
	# 		plateNumber = self.enPlateNumber.get()

	# 		cat = clsCarCategory.EmptyCarCategoryObject(loginInfo.DB_Mang).searchCategoryInfoInTableByName(self.cbCategory.get())
			
	# 		carCategoryID = cat[0]
			
	# 		if carCategoryID is None:
	# 			raise ValueError("Invalid category")

	# 		rntlPriceDay = Decimal(self.enPriceDay.get())
	# 		isAvailableForRent = 1 if self.cbIsAvail.get() == "yes" else 0
			
	# 		self.window.destroy()
	# 		car = clsCar(id,make, model, year, milage, plateNumber, carCategoryID, rntlPriceDay, isAvailableForRent, loginInfo.DB_Mang)
		
	# 		if car.addCarInfoToDB():
	# 			messagebox.showinfo("Success", "Car added successfully")
	# 		else:
	# 			messagebox.showerror("Error", "Failed to add car")

	# 	except ValueError as e: 
	# 		messagebox.showerror("error","Invalid Input" )

	
		 

 