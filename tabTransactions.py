
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from tabCommunButtons import clsAdminTab 
import loginInfo

from transaction import clsTransaction 
from winAddTransaction import clsWinAddTransaction
from winUpdateTransaction import clsWinUpdateTransaction
from winDeleteTransaction import clsWinDeleteTransaction

class clsTabTransactions(clsAdminTab):
	
	emptyTransaction = clsTransaction.EmptyTransactionObject(loginInfo.DB_Mang)

	def __init__(self,notebook,text) :
		super().__init__(notebook)
		self.transactionsTab = self.tab
		self.cbSearchBy.config(values=("Transaction id","Booking id","Return id"))
		self.transactionsTable = self._createTransactionsTable()

		notebook.add(self.transactionsTab, text=text)

 
	def _createTransactionsTable(self):
		self.transactionsTable = ttk.Treeview(self.transactionsTab ,show="headings")
		self.transactionsTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.67)

		self.transactionsTable["columns"] = ( "index", "Transaction id", "Booking id","return id","Total amount","Transaction date" )
		
		for column in self.transactionsTable["columns"]:
		
			self.transactionsTable.column(column, width=10,   anchor=tk.CENTER)
			self.transactionsTable.heading(column, text=column, anchor=tk.CENTER)
		data = self._getAllTransactionsInfo()
		if data is not None:
			self._fillTransactionsTable(data)
		 
		return self.transactionsTable
	
	def _fillTransactionsTable(self,data):
		counter = 1
		for item in data:
			self.transactionsTable.insert("", tk.END,  values=(counter,item[0], item[1], item[2], item[3],item[4]))
			counter += 1	
	def _getAllTransactionsInfo(self):
		data = clsTabTransactions.emptyTransaction.getAllTransactionInfoFromDBTransactionTables()
		return data
	
	
	def add(self):
		win = clsWinAddTransaction()
	
	def update(self):
		id = simpledialog.askstring("Transaction ID", "Enter Transaction ID to update:")
		if id is not None:
			trans = clsTabTransactions.emptyTransaction.searchTransactionInfoInTransTableByTransID(id)
			if (trans):
				win = clsWinUpdateTransaction(trans) 
			else:
				messagebox.showerror("Transaction ID","no Transaction exist with this ID: ")
	
	def delete(self):
		
		id = simpledialog.askstring("Transaction ID", "Enter Transaction ID to delete:")
		if id is not None:
			cust = clsTabTransactions.emptyTransaction.searchTransactionInfoInTransTableByTransID(id)
			if (cust):
				win = clsWinDeleteTransaction(cust)
			else:
				messagebox.showerror("Error","no Transaction exist with this ID: ")
	
	def search(self):
		srch = self.enID.get()
		try:		
			srch = int(srch)
			if (self.cbSearchBy.get() == "Booking id"):
				data = clsTabTransactions.emptyTransaction.searchTransactionInfoInTransTableByBookingID(srch)			 
			elif (self.cbSearchBy.get() == "return id"):
				data = clsTabTransactions.emptyTransaction.searchTransactionInfoInTransTableByReturnID(srch)			 
			else:
				data = clsTabTransactions.emptyTransaction.searchTransactionInfoInTransTableByTransID(srch)  
			
			if data:
				for item in self.transactionsTable.get_children():
					self.transactionsTable.delete(item)
				self._fillTransactionsTable(data)

				messagebox.showinfo("Transaction search","Transaction found")
			else :
				messagebox.showinfo("Transaction search","no Transaction found")
		except:
			messagebox.showerror("Transaction search","Just numbere are accepted!!")

	def refresh(self):
		for item in self.transactionsTable.get_children():
			self.transactionsTable.delete(item)
		data = self._getAllTransactionsInfo()
		if data is not None:
			self._fillTransactionsTable(data)
	 