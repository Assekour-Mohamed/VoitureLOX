import tkinter as tk
import datetime
from communMethods import generatID_ByDate
from validatingInputs import validateTransactionInputs
from transaction import clsTransaction
from tkinter import messagebox

import loginInfo

class clsWinUpdateTransaction:
	emptyTrans = clsTransaction.EmptyTransactionObject(loginInfo.DB_Mang)
	def __init__(self,trans) :
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("Update Transaction")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)
		self.window.grab_set()

		self.oldTransInfo = trans

		Label1 = tk.Label(self.window, text="UPDATING NEW TRANSACTION", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
		Label2 = tk.Label(self.window, text="Transaction ID:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2.place(relx=0.15, rely=0.24 )
		self.enTransID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enTransID.insert(0,self.oldTransInfo[0])
		self.enTransID.config(state="readonly")
		self.enTransID.place(relx=0.15, rely=0.3,  relheight=0.05)

		Label3 = tk.Label(self.window, text= "Booking id:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.4, rely=0.24 )
		self.enBookID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enBookID.insert(0,self.oldTransInfo[1])
		self.enBookID.place(relx=0.4, rely=0.3,  relheight=0.05)
		 
		Label4 = tk.Label(self.window, text="return id:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label4.place(relx=0.65, rely=0.24 )
		self.enRetrunID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enRetrunID.insert(0,self.oldTransInfo[2])
		self.enRetrunID.place(relx=0.65, rely=0.3,  relheight=0.05)
		

		Label5 = tk.Label(self.window, text="Total amount:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.15, rely=0.4 )
		self.enAmount = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enAmount.insert(0,self.oldTransInfo[3])
		self.enAmount.place(relx=0.15, rely=0.46,  relheight=0.05)
		
		Label5 = tk.Label(self.window, text="Transaction date:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.4, rely=0.4 )
		self.enTransDateTime = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enTransDateTime.insert(0,self.oldTransInfo[4])
		self.enTransDateTime.config(state="readonly")
		self.enTransDateTime.place(relx=0.4, rely=0.46,  relheight=0.05)

		 
		 
		 
		self.btnUpdateTransaction = tk.Button(self.window, text="Update", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.UpdateTransactionToDBtable)
		self.btnUpdateTransaction.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()

	def UpdateTransactionToDBtable(self):
		try:
			TransID = self.enTransID.get()
			BookID = self.enBookID.get().strip()
			RetrunID =  self.enRetrunID.get().strip()
			Amount = self.enAmount.get().strip()
			TransDateTime = self.enTransDateTime.get()
			validation = validateTransactionInputs(BookID,RetrunID,Amount)
			if validation == True:
				isBookingID = self.emptyTrans.searchTransactionInfoInTransTableByBookingID(int(BookID))
				isReturnID = self.emptyTrans.searchTransactionInfoInTransTableByReturnID(int(RetrunID))

				if  isBookingID is not None and isReturnID is not None:
					Transaction = clsTransaction(TransID,BookID,RetrunID,Amount,TransDateTime,loginInfo.DB_Mang)
					self.window.destroy()
					if Transaction.updateTransactionInfoInDB():
						messagebox.showinfo("info", "Transaction Updateed successfully")
						return True
					else:
						message = "Failed to Update Transaction"
				elif isBookingID == None:
					message = "Failed to Update Transaction no BOOKING record exist with this id!!"
				else:
					message = "Failed to Update Transaction no RETURNING record exist with this id!!"
			else:
				message = validation
		except ValueError as e: 
			message = "Invalid Input" 

		messagebox.showerror("Error", message)
		return False

		 

 