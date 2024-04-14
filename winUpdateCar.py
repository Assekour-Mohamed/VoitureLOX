import tkinter as tk
from tkinter import ttk
from decimal import Decimal

import validatingInputs
from car import clsCar
from carCategory import clsCarCategory
from tkinter import messagebox

import loginInfo

class clsWinUpdateCar:
	
	EmptyCar = clsCar.EmptyCar(loginInfo.DB_Mang)
	emptyCategor = clsCarCategory.EmptyCarCategoryObject(loginInfo.DB_Mang)

	def __init__(self, oldCar) :
		self.oldCarInfo = oldCar
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add car")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)
		self.window.grab_set()

		Label1 = tk.Label(self.window, text="UPDATE CAR", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		

		Labelid = tk.Label(self.window, text="Car id:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Labelid.place(relx=0.15, rely=0.24)
		self.enID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.insert(0, self.oldCarInfo[0])
		self.enID.config(state='readonly')
		self.enID.place(relx=0.15, rely=0.3,relheight=0.05)


		Label2 = tk.Label(self.window, text="Make:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2.place(relx=0.4, rely=0.24)
		self.enMake = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enMake.insert(0, self.oldCarInfo[1])	
		self.enMake.place(relx=0.4, rely=0.3,  relheight=0.05)

		Label3 = tk.Label(self.window, text="Model:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.65, rely=0.24)
		self.enModel = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enModel.insert(0, self.oldCarInfo[2])
		self.enModel.place(relx=0.65, rely=0.3,  relheight=0.05)
		 
		Label4 = tk.Label(self.window, text="year:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label4.place(relx=0.15, rely=0.4)
		self.enYear = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enYear.insert(0, self.oldCarInfo[3])
		self.enYear.place(relx=0.15, rely=0.46,  relheight=0.05)
		

				#( make, model, year, milage, plateNumber, carCategoryID, rntlPriceDay, isAvailableForRent,DB_CarManager , EmptyCar = False ):    
		Label5 = tk.Label(self.window, text="Milage:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.4, rely=0.4)
		self.enMilage = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enMilage.insert(0, self.oldCarInfo[4])
		self.enMilage.place(relx=0.4, rely=0.46,  relheight=0.05)

		Label6 = tk.Label(self.window, text="Plate number:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label6.place(relx=0.65, rely=0.4)
		self.enPlateNumber = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enPlateNumber.insert(0, self.oldCarInfo[5])
		self.enPlateNumber.place(relx=0.65, rely=0.46,  relheight=0.05)
		 
		Label7 = tk.Label(self.window, text="Category:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label7.place(relx=0.15, rely=0.56 )
		self.setCategoryCBOX(self.window)
		Label8 = tk.Label(self.window, text="Rantel Price (day):", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label8.place(relx=0.4, rely=0.56 )
		self.enPriceDay = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enPriceDay.insert(0, self.oldCarInfo[7])
		self.enPriceDay.place(relx=0.4, rely=0.62,  relheight=0.05)

		Label9 = tk.Label(self.window, text="is available:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label9.place(relx=0.65, rely=0.56 )
		self.cbIsAvail = ttk.Combobox(self.window, values=("yes","no"), state="readonly")
		if (self.oldCarInfo[8]==1):
			self.cbIsAvail.set("yes")
		else:
			self.cbIsAvail.set("no")
		self.cbIsAvail.place(relx=0.65, rely=0.62,  relheight=0.05)
		
		 		 
		self.btnAddCar = tk.Button(self.window, text="UPDATE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.updateCarInDBtable)
		self.btnAddCar.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()

	def	setCategoryCBOX(self,window):
		self.catsInfo = clsWinUpdateCar.emptyCategor.getAllCategorysInfoFromTable()
		self.catNames = [t[1] for t in self.catsInfo]
		self.cbCategory = ttk.Combobox(window, values=self.catNames, state="readonly")
		cat = clsWinUpdateCar.emptyCategor.searchCategoryInfoInTableById(self.oldCarInfo[6]) 
		self.cbCategory.set(cat.categoryName)
		self.cbCategory.place(relx=0.15, rely=0.62,  relheight=0.05  )
		
	def updateCarInDBtable(self):
		
		id = self.enID.get().strip()
		make = self.enMake.get().strip()
		model = self.enModel.get().strip()
		year = self.enYear.get().strip()
		milage =self.enMilage.get().strip()
		plateNumber = self.enPlateNumber.get().strip()
		carCategoryName = self.cbCategory.get()
		carCategory = self.emptyCategor.searchCategoryInfoInTableByName(carCategoryName)
		rntlPriceDay = self.enPriceDay.get().strip()
		isAvailableForRent = 1 if self.cbIsAvail.get() == "yes" else 0
		isValid = validatingInputs.validateCarInputs(id,make, model, year, milage, plateNumber , rntlPriceDay)
		if isValid ==True:
			self.window.destroy()
			car = clsCar(int(id),make, model, int(year), int(milage), plateNumber, carCategory.categoryID, Decimal(rntlPriceDay), isAvailableForRent,loginInfo.DB_Mang) 
			if car.updateCarInfoInDB():
				messagebox.showinfo("Success", "Car updated successfully")
			else:
				messagebox.showerror("Error", "Failed to update car")
		else:
			messagebox.showerror("Error", isValid)

