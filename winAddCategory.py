 


import tkinter as tk 

import communMethods
from tkinter import messagebox
from carCategory import clsCarCategory
import loginInfo

class clsWinAddCategory:
	EmptyCategory = clsCarCategory.EmptyCarCategoryObject(loginInfo.DB_Mang)
	def __init__(self) :
		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add category")
		self.window.geometry("450x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)
		self.window.grab_set()

		Label1 = tk.Label(self.window, text="ADDING NEW CATEGORY", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
 
		Label3 = tk.Label(self.window, text="ID:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.4, rely=0.24, relwidth=0.1)
		self.enID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.insert(0, communMethods.generatID_ByDate())
		self.enID.config(state="readonly")
		self.enID.place(relx=0.4, rely=0.3,  relheight=0.05)
		
		Label3 = tk.Label(self.window, text="NAME:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.4, rely=0.39, relwidth=0.1)
		self.enName = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enName.place(relx=0.4, rely=0.45,  relheight=0.05)
		 
		 
		 
		self.btnAddCategory = tk.Button(self.window, text="ADD", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.addCategoryToDBtable)
		self.btnAddCategory.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()

	def addCategoryToDBtable(self):
		try:
			name = self.enName.get()
			id = self.enID.get()
			if self.EmptyCategory.searchCategoryInfoInTableByName(name) == None:
				Category = clsCarCategory(id,name,loginInfo.DB_Mang)
				self.window.destroy()
				if Category.addCategoryInfoToDB():
					messagebox.showinfo("Success", "Category added successfully")
				else:
					messagebox.showerror("Error", "Failed to add Category")
			else :
					messagebox.showwarning("warning", "this category name is already exist!!")


		except ValueError as e:
			messagebox.showerror("error","Invalid Input" )

 