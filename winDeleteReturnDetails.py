 
import tkinter as tk 
from returnDetails import clsReturnDetails 
from tkinter import messagebox

from tkinter import ttk

import loginInfo

class clsWinDeleteReturnDetails:
	 
	emptyReturn = clsReturnDetails.EmptyReturnObject(loginInfo.DB_Mang)
	def __init__(self,returnInfo) :
		self.retrunInfo = returnInfo
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("Delete return record")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)

		Label1 = tk.Label(self.window, text="DELETE RETURN RECORD", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
 
		self._ReturnsTable = self._createReturnDetailssTable()

		Label2 = tk.Label(self.window, text="note : Transaction of this Returne Record will be also deleted!!", font="-family {Cascadia Mono} -size 10", background="white", foreground="red")
		Label2.place(relx=0.15, rely=0.6 )

		self.btnAddReturn = tk.Button(self.window, text="DELETE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.deleteReturnInDBtable)
		self.btnAddReturn.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()

	def _fillReturnDetailssTable(self,data): 
		counter = 1
		for item in data:
			self._ReturnsTable.insert("", tk.END,  values=(counter,item[0], item[1],item[2],item[3], item[4]))
			counter += 1	

	def _createReturnDetailssTable(self):
		self._ReturnsTable = ttk.Treeview(self.window ,show="headings")
		self._ReturnsTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.2)

		self._ReturnsTable["columns"] = ( "Index", "ID", "Return date", "Rental days", "Car milage", "FinalCheck notes")
		
		for column in self._ReturnsTable["columns"]:
		
			self._ReturnsTable.column(column, width=10,   anchor=tk.CENTER)
			self._ReturnsTable.heading(column, text=column, anchor=tk.CENTER)

		self._fillReturnDetailssTable((self.retrunInfo,))
		 
		return self._ReturnsTable
	
	 
	
	def deleteReturnInDBtable(self):
		id = self.retrunInfo[0]
		if clsWinDeleteReturnDetails.emptyReturn.deleteReturnInfoFromDB(id):
			messagebox.showinfo("Success", "Return deleted successfully")
		else:
			messagebox.showerror("Error", "Failed to delete Return")
	 
 

 