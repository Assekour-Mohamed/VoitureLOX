import tkinter as tk
from validatingInputs import validateCustomerInputs
from customer import clsCustomer
from tkinter import messagebox

import loginInfo

class clsWinAddCustomer:
	
	def __init__(self) :
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add customer")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)
		self.window.grab_set()

		Label1 = tk.Label(self.window, text="ADDING NEW CUSTOMER", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		

		Label2 = tk.Label(self.window, text="ID:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2.place(relx=0.15, rely=0.24 )
		self.enID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.place(relx=0.15, rely=0.3,  relheight=0.05)

		Label3 = tk.Label(self.window, text="Full name:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.4, rely=0.24 )
		self.enFullname = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enFullname.place(relx=0.4, rely=0.3,  relheight=0.05)
		 
		Label4 = tk.Label(self.window, text="Contact (phone):", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label4.place(relx=0.65, rely=0.24 )
		self.enContact = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enContact.place(relx=0.65, rely=0.3,  relheight=0.05)
		

				#( make, model, year, milage, plateNumber, carCategoryID, rntlPriceDay, isAvailableForRent,DB_CarManager , EmptyCar = False ):    
		Label5 = tk.Label(self.window, text="License number:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.15, rely=0.4 )
		self.enLicenseNumber = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enLicenseNumber.place(relx=0.15, rely=0.46,  relheight=0.05)

		 
		self.btnAddCar = tk.Button(self.window, text="ADD", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.addCustomerToDBtable)
		self.btnAddCar.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()

	def addCustomerToDBtable(self):
		try:
			id = self.enID.get().strip()
			fullname = self.enFullname.get().strip()
			conatct =  self.enContact.get().strip()
			licenseNumber = self.enLicenseNumber.get().strip()
			
			isValid = validateCustomerInputs(fullname,conatct,licenseNumber)
			if isValid ==True:
				customer = clsCustomer(id,fullname,conatct,licenseNumber,loginInfo.DB_Mang)
				self.window.destroy()
				if customer.addCustomerInfoToDB():
					messagebox.showinfo("Success", "Customer added successfully")
				else:
					messagebox.showerror("Error", "Failed to add customer")
			else:
				messagebox.showerror("Error", isValid)

		except ValueError as e: 
			messagebox.showerror("error","Invalid Input" )
		 

 