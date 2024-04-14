import tkinter as tk 
from customer import clsCustomer 
from tkinter import messagebox

from tkinter import ttk

import loginInfo

class clsWinDeleteTransaction:
	 
	emptyCustomer = clsCustomer.EmptyCustomerObject(loginInfo.DB_Mang)
	def __init__(self,Customer) :
		self.CustomerInfo = Customer
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add Customer")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)

		Label1 = tk.Label(self.window, text="DELETE CUSTOMER", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
 
		self._CustomersTable = self._createCustomersTable()

		Label2 = tk.Label(self.window, text="note : all reservation of this Customere will be also deleted!!", font="-family {Cascadia Mono} -size 10", background="white", foreground="red")
		Label2.place(relx=0.15, rely=0.6 )

		self.btnAddCustomer = tk.Button(self.window, text="DELETE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.deleteCustomerInDBtable)
		self.btnAddCustomer.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()
	

	def _createCustomersTable(self):
		self.customersTable = ttk.Treeview(self.window ,show="headings")
		self.customersTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.2)

		self.customersTable["columns"] = ( "index", "ID", "fullName","contactInfo","licenseNumber" )
		
		for column in self.customersTable["columns"]:
		
			self.customersTable.column(column, width=10,   anchor=tk.CENTER)
			self.customersTable.heading(column, text=column, anchor=tk.CENTER)
		
		self._fillCustomersTable((self.CustomerInfo,))
		return self.customersTable
	
	def _fillCustomersTable(self,data):
		counter = 1
		for item in data:
			self.customersTable.insert("", tk.END,  values=(counter,item[0], item[1], item[2], item[3]))
			counter += 1	
  
	def deleteCustomerInDBtable(self):
		id = self.CustomerInfo[0]
		if clsWinDeleteTransaction.emptyCustomer.deleteCustomerInfoFromDB(id):
			messagebox.showinfo("Success", "Customer deleted successfully")
		else:
			messagebox.showerror("Error", "Failed to delete Customer")
	 
 

 