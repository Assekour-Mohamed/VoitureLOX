

import tkinter as tk
from decimal import Decimal

import validatingInputs
import communMethods
from booking import clsBooking
from car import clsCar
from tkinter import messagebox
from datetime import datetime
import loginInfo

class clsWinAddBooking:
	
	emptyBooking = clsBooking.EmptyBookingObject(loginInfo.DB_Mang)
	emptyCar = clsCar.EmptyCar(loginInfo.DB_Mang)
	def __init__(self) :
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add Booking")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)
		self.window.grab_set()


		Label1 = tk.Label(self.window, text="ADDING NEW BOOKING", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
		
		Labelid = tk.Label(self.window, text="Booking id:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Labelid.place(relx=0.15, rely=0.24)
		self.enID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.insert(0, communMethods.generatID_ByDate())
		self.enID.config(state='readonly')
		self.enID.place(relx=0.15, rely=0.3,relheight=0.05)


		Label2 = tk.Label(self.window, text="Customer ID:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2.place(relx=0.4, rely=0.24)
		self.enCustomerID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enCustomerID.place(relx=0.4, rely=0.3,  relheight=0.05)

		Label3 = tk.Label(self.window, text="Car ID:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.65, rely=0.24)
		self.enCarID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enCarID.place(relx=0.65, rely=0.3,  relheight=0.05)
		 
		Label4 = tk.Label(self.window, text="Start Date:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label4.place(relx=0.15, rely=0.4)
		self.enStartDate = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enStartDate.bind('<FocusOut>', self.changeAmountValue)
		self.enStartDate.place(relx=0.15, rely=0.46,  relheight=0.05)
		
		Label5 = tk.Label(self.window, text="End Date:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.4, rely=0.4)
		self.enEndDate = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enEndDate.bind('<FocusOut>', self.changeAmountValue)
		self.enEndDate.place(relx=0.4, rely=0.46,  relheight=0.05)

		Label6 = tk.Label(self.window, text="Pick up location:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label6.place(relx=0.65, rely=0.4)
		self.enPupLoction = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enPupLoction.place(relx=0.65, rely=0.46,  relheight=0.05)
		 
		Label7 = tk.Label(self.window, text="Dro off location:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label7.place(relx=0.15, rely=0.56 )
		self.enDoffLction = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enDoffLction.place(relx=0.15, rely=0.62,  relheight=0.05 )
		 
		Label8 = tk.Label(self.window, text="Rantel Price (day):", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label8.place(relx=0.4, rely=0.56 )
		self.enPriceDay = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enPriceDay.place(relx=0.4, rely=0.62,  relheight=0.05)

		

		Label70 = tk.Label(self.window, text="Rantel Days number:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label70.place(relx=0.15, rely=0.72 )
		self.enRntlDays = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enRntlDays.place(relx=0.15, rely=0.78,  relheight=0.05 )
		
		Label9 = tk.Label(self.window, text="Due amount:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label9.place(relx=0.65, rely=0.56 )		
		self.enDueAmount = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enDueAmount.place(relx=0.65, rely=0.62,  relheight=0.05)
		
		Label10 = tk.Label(self.window, text="Check notes:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label10.place(relx=0.4, rely=0.72 )		
		self.enCheckNotes = tk.Text(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enCheckNotes.place(relx=0.4, rely=0.78,relheight= 0.05,relwidth=0.47  )
		
		 
		self.btnAddBooking = tk.Button(self.window, text="ADD", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.addBookingToDBtable)
		self.btnAddBooking.place(relx=0.283, rely=0.9, relwidth=0.451)
		self.window.focus_set()		 
		
	def changeAmountValue(self,event):
		end =self.enEndDate.get()
		start = self.enStartDate.get()
		valid = validatingInputs.validateStartAndEndDates(start,end)
		if valid == True:
			enddate = datetime.strptime(end,validatingInputs.dateformat).date() 
			startdate = datetime.strptime(start,validatingInputs.dateformat).date()

			car = emptyCar

			self.enDueAmount.insert(0,self.emptyBooking.calculDueAmount((enddate - startdate).days,PriceDay))
			self.enDueAmount.config(state="readonly")

		 


	def isCustomerAndCarIDExist(self,cstmr,car):
		isCustomerExist = self.emptyBooking.searchBookingInfoInDBbyCustomerID(cstmr)
		isCarExist = self.emptyBooking.searchBookingInfoInDBbyCustomerID(int(car))
		if isCustomerExist is not None and isCarExist is not None:
			return True
		elif isCustomerExist == None:
			message = "No CUSTOMER exist with this ID"
		else :
			message = "No CAR exist with this ID"


	def addBookingToDBtable(self):
		try:
			Bookingid = self.enID.get()
			CustomerID = self.enCustomerID.get().strip()			
			CarID = self.enCarID.get().strip()	 
			StartDate = self.enStartDate.get().strip()	
			EndDate = self.enEndDate.get().strip()	
			PupLoction = self.enPupLoction.get().strip()	
			DropOffLoction = self.enDoffLction.get().strip()	
			Days = self.enRntlDays.get().strip()	
			priceDay = self.enPriceDay.get().strip()	
			amount = self.enDueAmount.get().strip()	
			checkNotes = self.enCheckNotes.get("1.0","end-1c")
		 
			isValid = validatingInputs.validateBookingInputs(CustomerID,CarID,StartDate,EndDate,PupLoction,DropOffLoction,Days,priceDay,amount,checkNotes)
			
			if isValid == True: 	 
				checkMessage = self.isCustomerAndCarIDExist(CustomerID,CarID)
				if checkMessage == True:
					self.window.destroy()
					Booking = clsBooking(int(Bookingid),int(CustomerID),int(CarID),StartDate,EndDate,PupLoction,DropOffLoction,Days,Decimal(priceDay),Decimal(amount),checkNotes,loginInfo.DB_Mang)
					if Booking.addBookingInfoToDB():
						messagebox.showinfo("Success", "Booking added successfully")
					else:
						message = "Failed to add Booking record"
					return True
				else :
					message = checkMessage
			else:
				message = isValid

		except ValueError as e: 
			message = "error ouccurd" 
		messagebox.showerror("error",message)
		return False
		
	 
		
		
		