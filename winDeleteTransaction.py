import tkinter as tk 
from transaction import clsTransaction 
from tkinter import messagebox

from tkinter import ttk

import loginInfo

class clsWinDeleteTransaction:
	 
	emptyTransaction = clsTransaction.EmptyTransactionObject(loginInfo.DB_Mang)
	def __init__(self,Transaction) :
		self.TransactionInfo = Transaction
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("delete Transaction")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)

		Label1 = tk.Label(self.window, text="DELETE TRANSACTION", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
 
		self._TransactionsTable = self._createTransactionsTable()


		self.btndeleteTransaction = tk.Button(self.window, text="DELETE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.deleteTransactionInDBtable)
		self.btndeleteTransaction.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()
	

	def _createTransactionsTable(self):
		self.transactionsTable = ttk.Treeview(self.window ,show="headings")
		self.transactionsTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.2)

		self.transactionsTable["columns"] = ( "index", "Transaction id", "Booking id","return id","Total amount","Transaction date" )
		
		for column in self.transactionsTable["columns"]:
		
			self.transactionsTable.column(column, width=10,   anchor=tk.CENTER)
			self.transactionsTable.heading(column, text=column, anchor=tk.CENTER)
		data = self.TransactionInfo
		if data is not None:
			self._fillTransactionsTable((data,))
		 
		return self.transactionsTable
	
	def _fillTransactionsTable(self,data):
		counter = 1
		for item in data:
			self.transactionsTable.insert("", tk.END,  values=(counter,item[0], item[1], item[2], item[3],item[4]))
			counter += 1	
  
	def deleteTransactionInDBtable(self):
		id = self.TransactionInfo[0]
		if clsWinDeleteTransaction.emptyTransaction.deleteTransactionInfoFromDB(id):
			messagebox.showinfo("Success", "Transaction deleted successfully")
		else:
			messagebox.showerror("Error", "Failed to delete Transaction")
	 
 

 