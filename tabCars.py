import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

import loginInfo
from tabCommunButtons import clsAdminTab

from car import clsCar
from winAddCar import clsWinAddCar
from winUpdateCar import clsWinUpdateCar
from winDeleteCar import clsWinDeleteCar
from carCategory import clsCarCategory

class clsTabCars(clsAdminTab):
	EmptyCar = clsCar.EmptyCar(loginInfo.DB_Mang)
	EmptyCategory = clsCarCategory.EmptyCarCategoryObject(loginInfo.DB_Mang)
	
	def __init__(self,notebook,text) :
		super().__init__(notebook)
		self.carsTab = self.tab
		self.cbSearchBy.config(values=("Id","Make","Category id","Plate number"))

		self._CarsTable = self._createCarsTable()

		notebook.add(self.carsTab, text=text)

	def add(self):
		win = clsWinAddCar()
		
	def update(self):
		id = simpledialog.askstring("car ID", "Enter car ID to update:")
		if id is not None:
			car = clsTabCars.EmptyCar.searchCarInfoInCarstableByCarID(id)
			if (car):
				win = clsWinUpdateCar(car)
			else:
				messagebox.showerror("car ID","no car exict with this ID: ")

	def delete(self):
		id = simpledialog.askstring("car ID", "Enter car ID to delete:")
		if id is not None:
			car = clsTabCars.EmptyCar.searchCarInfoInCarstableByCarID(id)
			if (car):
				win = clsWinDeleteCar(car)
			else:
				messagebox.showerror("car ID","no car exist with this ID: ")

		 

	def search(self):
		srch = self.enID.get()
		srchBy = self.cbSearchBy.get()
		try:		
			data = None

			if (srchBy == "Id"):
				data = clsTabCars.EmptyCar.searchCarInfoInCarstableByCarID((int(srch)))
				data = [data,]
			elif (srchBy == "Make") :
				data = clsTabCars.EmptyCar.searchCarInfoInCarstableByMake(srch)
			elif (srchBy == "Category id"):
				data = clsTabCars.EmptyCar.searchCarInfoInCarstableBycarCategoryID(int(srch))
			elif (srchBy == "plate"):
				data = clsTabCars.EmptyCar.searchCarInfoInCarstableByPlate(srch)
				data = [data,]
			if data:
				for item in self._CarsTable.get_children():
					self._CarsTable.delete(item)
				self._fillCarsTable(data)
				messagebox.showinfo("car search","car found")
			else :
				messagebox.showinfo("car search","no car was found")
		except Exception as e:
			print("numbers only  " + str(e))
	 
	def refresh(self):
		for item in self._CarsTable.get_children():
			self._CarsTable.delete(item)
		data = self._getAllCarsInfo()
		if data is not None:
			self._fillCarsTable(data)
		
	def _getAllCarsInfo(self):
		data = clsTabCars.EmptyCar.getAllCarsInfoFromDBcarsTable()
		return data
	def _fillCarsTable(self,data): 
		counter = 1
		for item in data:
			if item[8] == 1:
				v = "yes"
			else :
				v = "no"
			self._CarsTable.insert("", tk.END,  values=(counter,item[0], item[1],item[2],item[3],item[7],v,item[6],item[4],item[5]))
			counter += 1	
	def _createCarsTable(self):
		self._CarsTable = ttk.Treeview(self.carsTab ,show="headings")
		self._CarsTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.67)

		self._CarsTable["columns"] = ( "number", "ID", "make", "model", "year", "Price Day", "Available","CategoryID", "milage" , "plate Number")
		
		
		for column in self._CarsTable["columns"]:
			if column =="number":
				self._CarsTable.column("number", width=20, minwidth=20 )
				self._CarsTable.heading("number", text="number", anchor=tk.W)

			self._CarsTable.column(column, width=10,   anchor=tk.CENTER)
			self._CarsTable.heading(column, text=column, anchor=tk.CENTER)
		data =self._getAllCarsInfo()
		if data is not None:
			self._fillCarsTable(data)
					 
		return self._CarsTable
	
   