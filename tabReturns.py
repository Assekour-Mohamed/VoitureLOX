 

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
 
import loginInfo
from tabCommunButtons import clsAdminTab

from returnDetails import clsReturnDetails
from winAddReturnDetails import clsWinAddReturnDetails
from winUpdateReturnDetails import clsWinUpdateReturnDetails
from winDeleteReturnDetails import clsWinDeleteReturnDetails
 
class clsTabReturns(clsAdminTab):
	EmptyReturnDetails = clsReturnDetails.EmptyReturnObject(loginInfo.DB_Mang)

	def __init__(self,notebook,text) :
		super().__init__(notebook)
		self.ReturnTab = self.tab
		self.cbSearchBy.set("Return id")

		self._ReturnsTable = self._createReturnDetailssTable()

		notebook.add(self.ReturnTab, text=text)

	def add(self):
		win = clsWinAddReturnDetails()
		
	def update(self):
		id = simpledialog.askstring("ReturnDetails ID", "Enter ReturnDetails ID to update:")
		returnToUpdate = clsTabReturns.EmptyReturnDetails.seaechReturnInfoInReturnsTableRyReturnID(id)
		if returnToUpdate is not None:		
			win = clsWinUpdateReturnDetails(returnToUpdate)
		else:
			messagebox.showerror("ReturnDetails ID","no ReturnDetails exict with this ID: ")

	def delete(self):
		id = simpledialog.askstring("ReturnDetails ID", "Enter ReturnDetails ID to delete:")
		if id is not None:
			ReturnDetails = clsTabReturns.EmptyReturnDetails.seaechReturnInfoInReturnsTableRyReturnID(id)
			if (ReturnDetails):
				win = clsWinDeleteReturnDetails(ReturnDetails)
			else:
				messagebox.showerror("ReturnDetails ID","no ReturnDetails exist with this ID: ")

	def search(self):
		id = self.enID.get()
		try:		
			 
			data = clsTabReturns.EmptyReturnDetails.seaechReturnInfoInReturnsTableRyReturnID(int(id))
			if data:
				for item in self._ReturnsTable.get_children():
					self._ReturnsTable.delete(item)
				self._fillReturnDetailssTable((data,))
				messagebox.showinfo("ReturnDetails search","ReturnDetails found")
			else :
				messagebox.showinfo("ReturnDetails search","No return details exist with this id")
		except Exception as e:
				messagebox.showinfo("ReturnDetails search","No return details exist with this id")
	 
	def refresh(self):
		for item in self._ReturnsTable.get_children():
			self._ReturnsTable.delete(item)
		data = self._getAllReturnDetailssInfo()
		if data is not None:
			self._fillReturnDetailssTable(data)
		
	def _getAllReturnDetailssInfo(self):
		data = clsTabReturns.EmptyReturnDetails.getAllReturnInfoInReturnsTable()
		return data
	def _fillReturnDetailssTable(self,data): 
		counter = 1
		for item in data:
			self._ReturnsTable.insert("", tk.END,  values=(counter,item[0], item[1],item[2],item[3], item[4]))
			counter += 1	

	def _createReturnDetailssTable(self):
		self._ReturnsTable = ttk.Treeview(self.ReturnTab ,show="headings")
		self._ReturnsTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.67)

		self._ReturnsTable["columns"] = ( "Index", "ID", "Return date", "Rental days", "Car milage", "FinalCheck notes")
		
		for column in self._ReturnsTable["columns"]:
		
			self._ReturnsTable.column(column, width=10,   anchor=tk.CENTER)
			self._ReturnsTable.heading(column, text=column, anchor=tk.CENTER)
		data =self._getAllReturnDetailssInfo()

		if data is not None:
			self._fillReturnDetailssTable(data)
		 
		return self._ReturnsTable
	
   