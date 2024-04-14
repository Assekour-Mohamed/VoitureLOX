 

import tkinter as tk 
from validatingInputs import validateReturnInputs

from returnDetails import clsReturnDetails
from tkinter import messagebox

import loginInfo

class clsWinUpdateReturnDetails:
	
	def __init__(self,returninfo) :
		self.returnInfo = returninfo

	
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("Update return")
		self.window.geometry("750x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)

		Label1 = tk.Label(self.window, text="UPDATEING RETURN RECORD", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		

		Label2 = tk.Label(self.window, text="ID:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2.place(relx=0.15, rely=0.24 )
		self.enID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.insert(0,self.returnInfo[0])
		self.enID.config(state="readonly")
		self.enID.place(relx=0.15, rely=0.3,  relheight=0.05)

		Label3 = tk.Label(self.window, text="Return date:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.4, rely=0.24 )
		self.enReturnDate = tk.Entry(self.window,background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enReturnDate.insert(0,self.returnInfo[1])
		self.enReturnDate.place(relx=0.4, rely=0.3,  relheight=0.05)
		 
		Label4 = tk.Label(self.window, text="Rental days:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label4.place(relx=0.65, rely=0.24 )
		self.enRentalDays = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enRentalDays.insert(0,self.returnInfo[2])		
		self.enRentalDays.place(relx=0.65, rely=0.3,  relheight=0.05)
		
		
		Label5 = tk.Label(self.window, text="Car milage", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.15, rely=0.4 )
		self.enCarMalge = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enCarMalge.insert(0,self.returnInfo[3])
		self.enCarMalge.place(relx=0.15, rely=0.46,  relheight=0.05)
		
		Label5 = tk.Label(self.window, text="Final check notes", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label5.place(relx=0.4, rely=0.4 )
		self.enCheckNotes = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enCheckNotes.insert(0,self.returnInfo[4])		
		self.enCheckNotes.place(relx=0.4, rely=0.46,  relheight=0.05)
 
		self.btnUpdateReturn = tk.Button(self.window, text="UPDATE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.updatereturnInDB)
		self.btnUpdateReturn.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()
	 
	
	def updatereturnInDB(self):
		try:
			id = self.enID.get().strip()
			returnDate = self.enReturnDate.get().strip()
			rntelDays = self.enRentalDays.get().strip()
			milage = self.enCarMalge.get().strip()
			checkNotes = self.enCheckNotes.get().strip()
			isvalid = validateReturnInputs(returnDate, rntelDays,milage,checkNotes) 
			if isvalid == True:
				retrn = clsReturnDetails(int(id),returnDate,int(rntelDays),int(milage),checkNotes,loginInfo.DB_Mang)
				self.window.destroy()
				if retrn.updateReturnInfoInDB():
					messagebox.showinfo("Success", "Return record updated successfully")
					retrn.updateCarMilageInCarsTable()
				else:
					messagebox.showerror("Error", "Failed to update Return record")
			else:
					messagebox.showerror("Error",isvalid)
			

		except ValueError as e: 
			messagebox.showerror("error","Invalid Input" )
		 
	 