class clsWinDeleteBooking:
  def __init__(self,bookingInfo) -> None:
    print("not created yet")

import tkinter as tk 
from booking import clsBooking 
from tkinter import messagebox

from tkinter import ttk

import loginInfo

class clsWinDeleteBooking:
	 
	emptyBooking = clsBooking.EmptyBookingObject(loginInfo.DB_Mang)
	def __init__(self,Booking) :
		self.BookingInfo = Booking
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("Delete Booking")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)

		Label1 = tk.Label(self.window, text="DELETE BOOKING", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
 
		self._BookingsTable = self._createBookingsTable()

		Label2 = tk.Label(self.window, text="note : all TRANSACTION width this booking ID will be also deleted!!", font="-family {Cascadia Mono} -size 10", background="white", foreground="red")
		Label2.place(relx=0.15, rely=0.6 )

		self.btnAddBooking = tk.Button(self.window, text="DELETE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.deleteBookingInDBtable)
		self.btnAddBooking.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()
	

	def _fillBookingsTable(self,data): 
		counter = 1
		for item in data:			
			self._BookingsTable.insert("", tk.END,  values=(counter,item[0], item[1],item[2],item[3], item[4],item[5],item[6],item[7],item[8],item[9],item[10]))
			
			counter += 1	

	def _createBookingsTable(self):
		self._BookingsTable = ttk.Treeview(self.window ,show="headings")
		self._BookingsTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.2)

		self._BookingsTable["columns"] = ("index","Book ID", "Cstmr ID", "CarID", "StartDate","EndDate", "Pickup", "DropOff", "Days", "PriceDay", "DueAmount", "CheckNotes")

		for column in self._BookingsTable["columns"]:
			 
				self._BookingsTable.column(column,width="10"  ,   anchor=tk.CENTER)
				self._BookingsTable.heading(column, text=column, anchor=tk.CENTER)
		
		self._BookingsTable.column("index",width="5"  , anchor=tk.CENTER)
		self._BookingsTable.heading("index", text="index", anchor=tk.CENTER)

		self._fillBookingsTable((self.BookingInfo,))
		 
		return self._BookingsTable
  
	def deleteBookingInDBtable(self):
		id = self.BookingInfo[0]
		if clsWinDeleteBooking.emptyBooking.deleteBookingInfoFromDB(id):
			messagebox.showinfo("Success", "Booking deleted successfully")
		else:
			messagebox.showerror("Error", "Failed to delete Booking")
	 
 

 