 

import tkinter as tk 

from tkinter import messagebox
from carCategory import clsCarCategory
import loginInfo

class clsWinUpdateCategory:
	
	def __init__(self, oldCatinfo) :
		self.oldCatinfo = oldCatinfo

		self.window = tk.Toplevel()
		self.window.configure(background='#002953')
		self.window.title("add category")
		self.window.geometry("450x454+221+129")
		self.window.maxsize(1370, 749)
		self.window.minsize(120, 1)
 
		Label1 = tk.Label(self.window, text="UPDATION CATEGORY", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place( x=0, y=10, relwidth=1, relheight=0.136)
		
		Label3 = tk.Label(self.window, text="ID:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.4, rely=0.24, relwidth=0.1)
		self.enID = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.insert(0,self.oldCatinfo.categoryID)
		self.enID.config(state="readonly")
		self.enID.place(relx=0.4, rely=0.3,  relheight=0.05)
 
	 
		Label3 = tk.Label(self.window, text="NAME:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label3.place(relx=0.4, rely=0.39, relwidth=0.1)
		self.enName = tk.Entry(self.window, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enName.place(relx=0.4, rely=0.45,  relheight=0.05)
		self.enName.insert(0,self.oldCatinfo.categoryName)
		 
		 
		self.btnAddCategory = tk.Button(self.window, text="UPDATE", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.updateCategoryInDBtable)
		self.btnAddCategory.place(relx=0.283, rely=0.859, relwidth=0.451)
		self.window.focus_set()

	def updateCategoryInDBtable(self):
		name = self.enName.get()
		id = self.oldCatinfo.categoryID
		Category = clsCarCategory(id,name,loginInfo.DB_Mang)
		
		if Category.updateCategoryInfoInDB():
			messagebox.showinfo("Success", "Category updated successfully")
		else:
			messagebox.showerror("Error", "Failed to update Category")
 
 