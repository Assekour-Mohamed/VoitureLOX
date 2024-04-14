import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
 
import loginInfo
from tabCommunButtons import clsAdminTab

from booking import clsBooking
from winAddBooking import clsWinAddBooking
from winUpdateBooking import clsWinUpdateBooking
from winDeleteBooking import clsWinDeleteBooking
 
class clsTabBookings(clsAdminTab):
	EmptyBooking = clsBooking.EmptyBookingObject(loginInfo.DB_Mang)

	def __init__(self,notebook,text) :
		super().__init__(notebook)
		self.BookingTab = self.tab
		self.cbSearchBy.config(values=("Booking ID","Customer ID ","Car ID"))

		self._BookingsTable = self._createBookingsTable()

		notebook.add(self.BookingTab, text=text)

	def add(self):
		win = clsWinAddBooking()
		
	def update(self):
		id = simpledialog.askstring("Booking ID", "Enter Booking ID to update:")
		if id :
			BookingToUpdate = clsTabBookings.EmptyBooking.searchBookingInfoInDBbyBookingID(id)
			if BookingToUpdate is not None:		
				win = clsWinUpdateBooking(BookingToUpdate)
			else:
				messagebox.showerror("Booking ID","no Booking exict with this ID: ")

	def delete(self):
		id = simpledialog.askstring("Booking ID", "Enter Booking ID to delete:")
		if id is not None:
			Booking = clsTabBookings.EmptyBooking.searchBookingInfoInDBbyBookingID(id)
			if (Booking):
				win = clsWinDeleteBooking(Booking)
			else:
				messagebox.showerror("Booking ID","no Booking exist with this ID: ")

	def search(self):
		id = self.enID.get()
		try:		
			srchby = self.cbSearchBy.get()
			if (srchby =="Customer ID"):
				data = clsTabBookings.EmptyBooking.searchBookingInfoInDBbyCustomerID(id)
			elif (srchby =="Car ID"):
				data = clsTabBookings.EmptyBooking.searchBookingInfoInDBbyCarID(int(id))
			else :
				data = clsTabBookings.EmptyBooking.searchBookingInfoInDBbyBookingID(int(id))
				data =(data,)
			if data:
				for item in self._BookingsTable.get_children():
					self._BookingsTable.delete(item)
				self._fillBookingsTable(data)
				messagebox.showinfo("Booking search","Booking found")
			else :
				messagebox.showinfo("Booking search","No Booking exist with this id")
		except Exception as e:
				messagebox.showinfo("Booking search","No Booking exist with this id")
	 
	def refresh(self):

		for item in self._BookingsTable.get_children():
			self._BookingsTable.delete(item)
		data = self._getAllBookingsInfo()
		if data is not None:
			self._fillBookingsTable(data)
		
	def _getAllBookingsInfo(self):
		data = clsTabBookings.EmptyBooking.getAllBookingsInfoFromDBBookingsTable()
		return data
	
	def _fillBookingsTable(self,data): 
		counter = 1
		for item in data:			
			self._BookingsTable.insert("", tk.END,  values=(counter,item[0], item[1],item[2],item[3], item[4],item[5],item[6],item[7],item[8],item[9],item[10]))
			
			counter += 1	

	def _createBookingsTable(self):
		self._BookingsTable = ttk.Treeview(self.BookingTab ,show="headings")
		self._BookingsTable.place(relx=0.06, rely=0.2,relwidth=0.88, relheight=0.67)

		self._BookingsTable["columns"] = ("index","Book ID", "Cstmr ID", "CarID", "StartDate","EndDate", "Pickup", "DropOff", "Days", "PriceDay", "DueAmount", "CheckNotes")

		for column in self._BookingsTable["columns"]:
			 
				self._BookingsTable.column(column,width="10"  ,   anchor=tk.CENTER)
				self._BookingsTable.heading(column, text=column, anchor=tk.CENTER)
		
		self._BookingsTable.column("index",width="5"  , anchor=tk.CENTER)
		self._BookingsTable.heading("index", text="index", anchor=tk.CENTER)
		data =self._getAllBookingsInfo()

		if data is not None:
			self._fillBookingsTable(data)

		return self._BookingsTable
	
	 