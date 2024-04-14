import tkinter as tk
from tkinter import ttk
import Pmw
	
 
import tkinter as tk
from PIL import Image, ImageTk

class clsAdminTab:
	 
	def __init__(self,notebook) :
		
		style = ttk.Style()
		style.configure('My.TFrame', background='#002953')
		
		self.tab = ttk.Frame(notebook,style="My.TFrame" )
		
		
		image = Image.open(r"image\add.png")
		image = image.resize((20,20))
		imgAdd = ImageTk.PhotoImage(image)
		self.btnAdd = tk.Button(self.tab, text="",image =imgAdd,compound=tk.RIGHT, padx=30, font="-family {Cascadia Mono} -size 10 ", command=self.add )
		self.btnAdd.place(relx=0.02, rely=0.015,relwidth=0.15 , relheight=0.0648)
		self.btnAdd.image = imgAdd
		tooltip = Pmw.Balloon(self.tab)
		tooltip.bind(self.btnAdd,"Add new record")

		
		image = Image.open(r"image\update.png")
		image = image.resize((20,20))
		imgUpdate = ImageTk.PhotoImage(image)
		self.btnUpdate = tk.Button(self.tab, text="",image =imgUpdate,compound=tk.RIGHT, padx=30, font="-family {Cascadia Mono} -size 10 " , command=self.update)
		self.btnUpdate.place(relx=0.177, rely=0.015,relwidth=0.15, relheight=0.0648 )
		self.btnUpdate.image = imgUpdate
		tooltip = Pmw.Balloon(self.tab)
		tooltip.bind(self.btnUpdate,"Update record")



		image = Image.open(r"image\delete.png")
		image = image.resize((20,20))
		imgDelete = ImageTk.PhotoImage(image)
		self.btnDelete = tk.Button(self.tab, text="",image =imgDelete,compound=tk.RIGHT, padx=30, font="-family {Cascadia Mono} -size 10 " , command=self.delete)
		self.btnDelete.place(relx=0.335, rely=0.015,relwidth=0.15, relheight=0.0648 )
		self.btnDelete.image = imgDelete
		tooltip = Pmw.Balloon(self.tab)
		tooltip.bind(self.btnDelete,"Delete record")

		self.setupSearch()

		
		image = Image.open(r"image\refresh.png")
		image = image.resize((20,20))
		imgRefrsh = ImageTk.PhotoImage(image)
		self.btnRefrsh = tk.Button(self.tab, text="",image =imgRefrsh,compound=tk.RIGHT, padx=30, font="-family {Cascadia Mono} -size 10  ", command=self.refresh)
		self.btnRefrsh.place( relx=0.46, rely=0.9,relwidth=0.15 , relheight=0.0648)
		self.btnRefrsh.image = imgRefrsh
		tooltip = Pmw.Balloon(self.tab)
		tooltip.bind(self.btnRefrsh,"Refresh and show all records")


	
	def setupSearch(self):
		self.enID = tk.Entry(self.tab, background="white", font="-family {Cascadia Mono} -size 10", foreground="#000000")
		self.enID.place(relx=0.6, rely=0.015, relwidth=0.1, relheight=0.0648)
		 
		self.cbSearchBy = ttk.Combobox(self.tab, state="readonly" )
		self.cbSearchBy.set("Search by:")
	 
		self.cbSearchBy.place(relx=0.7, rely=0.015 , relheight=0.0648 )
		
		image = Image.open(r"image\search.gif")
		image = image.resize((20,20))
		imgSearch = ImageTk.PhotoImage(image)

		self.btnSearch = tk.Button(self.tab, text="",image=imgSearch, font="-family {Cascadia Mono} -size 10 ", command=self.search)
		self.btnSearch.place( relx=0.87, rely=0.015 ,relwidth=0.08, relheight=0.0648)
		tooltip = Pmw.Balloon(self.tab)
		tooltip.bind(self.btnSearch,"Search for record")
		self.btnSearch.image = imgSearch

		
	


	def add():
		pass
	def update():
		pass
	def delete():
		pass
	def search():
		pass
	def refresh():
		pass



		 
	 