import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
 
import loginInfo
from carCategory import clsCarCategory

from winAddCategory import clsWinAddCategory
from winUpdateCategory import clsWinUpdateCategory
from winDeleteCategory import clsWinDeleteCategory

from tabCommunButtons import clsAdminTab

class clsTabCategory(clsAdminTab):
	
	EmptyCategory = clsCarCategory.EmptyCarCategoryObject(loginInfo.DB_Mang)

	def __init__(self,notebook,text) :
		super().__init__(notebook)
		self.categorytab = self.tab
		self.cbSearchBy.config(values=("Id","Name"))
		self._categoreisTable = self._createCategoriesTable()

		notebook.add(self.categorytab, text=text)


	def _createCategoriesTable(self):
		self._categoreisTable = ttk.Treeview(self.categorytab ,show="headings")
		self._categoreisTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.67)

		self._categoreisTable["columns"] = ( "number", "ID", "Name" )
		
		for column in self._categoreisTable["columns"]:
			if column =="number":
				self._categoreisTable.column("number", width=20, minwidth=20 )
				self._categoreisTable.heading("number", text="number", anchor=tk.W)

			self._categoreisTable.column(column, width=10,   anchor=tk.CENTER)
			self._categoreisTable.heading(column, text=column, anchor=tk.CENTER)
		data = self._getAllCtegoriesInfo()
		if data is not None:
			self._fillCategoriesTable(data)
		 
		return self._categoreisTable
	
	def _fillCategoriesTable(self,data):
		
		counter = 1
		for item in data:
			self._categoreisTable.insert("", tk.END,  values=(counter,item[0], item[1]))
			counter += 1	
	def _getAllCtegoriesInfo(self):
		data = clsTabCategory.EmptyCategory.getAllCategorysInfoFromTable()
		return data
	
	
	def add(self):
		cat = clsWinAddCategory()
	
	def update(self):
		id = simpledialog.askstring("category ID", "Enter category ID to update:")
		category = clsTabCategory.EmptyCategory.searchCategoryInfoInTableById(id)
		 
		if (category):
			win = clsWinUpdateCategory(category)
		else:
			messagebox.showerror("categroy ID","no categroy exict with this ID: ")
	
	def delete(self):
		
		id = simpledialog.askstring("category ID", "Enter category ID to delete:")
		try:
			cat = clsTabCategory.EmptyCategory.searchCategoryInfoInTableById(int(id))

			if (cat):
				win = clsWinDeleteCategory(cat)
			else:
				messagebox.showerror("categroy ID","no categroy exict with this ID: ")
		except:
			messagebox.showerror("error","Invalid Input" )

	
	def showCategoryRecord(self,category):
		if category.categoryID != -1:
			for item in self._categoreisTable.get_children():
				self._categoreisTable.delete(item)
			self._fillCategoriesTable([category.toTuple()])
			messagebox.showinfo("category search","category found")
		else :
			messagebox.showinfo("category search","no category found")

	def search(self):
		srch = self.enID.get()
	
		if (self.cbSearchBy.get() == "Name"):
			category = clsTabCategory.EmptyCategory.searchCategoryInfoInTableByName(srch)
			self.showCategoryRecord(category)
		else:
			try:
				category = clsTabCategory.EmptyCategory.searchCategoryInfoInTableById(int(srch))
				self.showCategoryRecord(category)
			except:
				messagebox.showinfo("category search","no category found invalid input")

		
	def refresh(self):
		for item in self._categoreisTable.get_children():
			self._categoreisTable.delete(item)
		data = self._getAllCtegoriesInfo()
		if data is not None:
			self._fillCategoriesTable(data)
	 