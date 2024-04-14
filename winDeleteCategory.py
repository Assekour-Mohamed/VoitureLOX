 
import tkinter as tk
from tkinter import ttk
from decimal import Decimal

from car import clsCar
from carCategory import clsCarCategory
from tkinter import messagebox

import loginInfo

class clsWinDeleteCategory:
	 
	EmptyCategory = clsCarCategory.EmptyCarCategoryObject(loginInfo.DB_Mang)
	def __init__(self,catinfo) :
		self.categoryInfo = catinfo
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add car")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)

		Label1 = tk.Label(self.window, text="DELETE CATEGORY", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		

		 
		Label2 = tk.Label(self.window, text="note : all cars with the same category ID will be also deleted!!", font="-family {Cascadia Mono} -size 10", background="white", foreground="red")
		Label2.place(relx=0.15, rely=0.7 )
 
		self.btnAddcategory = tk.Button(self.window, text="DELETE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.deletecategoryInDBtable)
		self.btnAddcategory.place(relx=0.283, rely=0.859, relwidth=0.451)


		self._categoreisTable = ttk.Treeview(self.window ,show="headings")
		self._categoreisTable.place(relx=0.1, rely=0.35,relwidth=0.8, relheight=0.2)

		self._setUpCategoriesTable()
		self.window.focus_set()


	def _setUpCategoriesTable(self):
		
		self._categoreisTable["columns"] = ( "number", "ID", "name" )
		
		for column in self._categoreisTable["columns"]:
			 
			self._categoreisTable.column(column, width=10,   anchor=tk.CENTER)
			self._categoreisTable.heading(column, text=column, anchor=tk.CENTER)
		
		self._fillCategoriesTable([self.categoryInfo.toTuple()])
		
	def _fillCategoriesTable(self,data):
		counter = 1
		for item in data:
			self._categoreisTable.insert("", tk.END,  values=(counter,item[0], item[1]))
			counter += 1	
  
	def deletecategoryInDBtable(self):
		
		
			if clsWinDeleteCategory.EmptyCategory.deleteCategoryInfoFromDB(self.categoryInfo.categoryID):
				messagebox.showinfo("Success", "category deleted successfully")
			else:
				messagebox.showerror("Error", "Failed to delete category")
	 

 