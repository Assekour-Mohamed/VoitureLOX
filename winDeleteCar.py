import tkinter as tk 
from car import clsCar 
from tkinter import messagebox

from tkinter import ttk

import loginInfo

class clsWinDeleteCar:
	 
	EmptyCar = clsCar.EmptyCar(loginInfo.DB_Mang)
	def __init__(self,car) :
		self.carInfo = car
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add car")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)

		Label1 = tk.Label(self.window, text="DELETE CAR", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		

		
		 
		
 
		self._CarsTable = self._createCarsTable()

		Label2 = tk.Label(self.window, text="note : all reservation with this care will be also deleted!!", font="-family {Cascadia Mono} -size 10", background="white", foreground="red")
		Label2.place(relx=0.15, rely=0.6 )

		self.btnAddCar = tk.Button(self.window, text="DELETE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.deleteCarInDBtable)
		self.btnAddCar.place(relx=0.283, rely=0.859, relwidth=0.451)
	
		self.window.focus_set()


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
		self._CarsTable = ttk.Treeview(self.window ,show="headings")
		self._CarsTable.place(relx=0.06, rely=0.3,relwidth=0.9, relheight=0.2)

		self._CarsTable["columns"] = ( "number", "ID", "make", "model", "year", "Price Day", "Available","CategoryID", "milage" , "plate Number")
		
		
		for column in self._CarsTable["columns"]:
			if column =="number":
				self._CarsTable.column("number", width=20, minwidth=20 )
				self._CarsTable.heading("number", text="number", anchor=tk.W)

			self._CarsTable.column(column, width=10,   anchor=tk.CENTER)
			self._CarsTable.heading(column, text=column, anchor=tk.CENTER)
		
		self._fillCarsTable((self.carInfo,))
		return self._CarsTable
	
	def deleteCarInDBtable(self):
		try:
			id = self.carInfo[0]
			if clsWinDeleteCar.EmptyCar.deleteCarInfoFromDB(id):
				messagebox.showinfo("Success", "Car deleted successfully")
			else:
				messagebox.showerror("Error", "Failed to delete car")
		except:
			messagebox.showerror("error","Invalid Input" )

 

 