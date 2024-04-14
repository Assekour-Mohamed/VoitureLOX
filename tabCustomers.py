
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from tabCommunButtons import clsAdminTab 
import loginInfo

from customer import clsCustomer
from winAddCustomer import clsWinAddCustomer
from winUpdateCustomer import clswinUpdateCustomer
from winDeleteCustomer import clsWinDeleteTransaction


class clsTabCustomers(clsAdminTab):
	
	emptyCustomer = clsCustomer.EmptyCustomerObject(loginInfo.DB_Mang)

	def __init__(self,notebook,text) :
		super().__init__(notebook)
		self.customersTab = self.tab
		self.cbSearchBy.config(values=("Id","Fullname","License number"))
		self.customersTable = self._createCustomersTable()

		notebook.add(self.customersTab, text=text)

 
	def _createCustomersTable(self):
		self.customersTable = ttk.Treeview(self.customersTab ,show="headings")
		self.customersTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.67)

		self.customersTable["columns"] = ( "index", "ID", "fullName","contactInfo","licenseNumber" )
		
		for column in self.customersTable["columns"]:
		
			self.customersTable.column(column, width=10,   anchor=tk.CENTER)
			self.customersTable.heading(column, text=column, anchor=tk.CENTER)
		
		data =self._getAllCustomersInfo()
		if data is not None:
			self._fillCustomersTable(data)
		 
		return self.customersTable
	
	def _fillCustomersTable(self,data):
		counter = 1
		for item in data:
			self.customersTable.insert("", tk.END,  values=(counter,item[0], item[1], item[2], item[3]))
			counter += 1	
	def _getAllCustomersInfo(self):
		data = clsTabCustomers.emptyCustomer.getAllCustomerInfoFromCustomesTable()
		return data
	
	
	def add(self):
		win = clsWinAddCustomer()
	
	def update(self):
		id = simpledialog.askstring("Customer ID", "Enter customer ID to update:")
		if id is not None:
			ctmr = clsTabCustomers.emptyCustomer.searchCustomerInfoInCustomersTaleByCustomerID(id)
			if (ctmr):
				win = clswinUpdateCustomer(ctmr) 
			else:
				messagebox.showerror("customer ID","no customer exict with this ID: ")
	
	def delete(self):
		
		id = simpledialog.askstring("Customer ID", "Enter Customer ID to delete:")
		if id is not None:
			cust = clsTabCustomers.emptyCustomer.searchCustomerInfoInCustomersTaleByCustomerID(id)
			if (cust):
				win = clsWinDeleteTransaction(cust)
			else:
				messagebox.showerror("customer ID","no customer exist with this ID: ")
	
	def search(self):
		srch = self.enID.get()
		try:		
			if (self.cbSearchBy.get() == "Id"):
				data = clsTabCustomers.emptyCustomer.searchCustomerInfoInCustomersTaleByCustomerID(srch)  
			elif (self.cbSearchBy.get() == "Fullname"):
				data = clsTabCustomers.emptyCustomer.searchCustomerInfoInCustomersTaleByFullname(srch)			 
			elif (self.cbSearchBy.get() == "License number"):
				data = clsTabCustomers.emptyCustomer.searchCustomerInfoInCustomersTaleByLicenseNumber(srch)			 
			
			if data:
				for item in self.customersTable.get_children():
					self.customersTable.delete(item)
				self._fillCustomersTable((data,))

				messagebox.showinfo("Customer search","Customer found")
			else :
				messagebox.showinfo("Customer search","no Customer found")
		except:
			print("numbers only")

	def refresh(self):
		for item in self.customersTable.get_children():
			self.customersTable.delete(item)
		data = self._getAllCustomersInfo()
		if data is not None:
			self._fillCustomersTable(data)
	 