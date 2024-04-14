import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk 
from tabCars import clsTabCars
from tabCarCategory import clsTabCategory
from tabBookings import clsTabBookings
from tabCustomers import clsTabCustomers
from tabReturns import clsTabReturns
from tabTransactions import clsTabTransactions
class clsAdminHome  : 
 
	def __init__(self,root):	
		self.root = root
		root.configure()
		root.title("admin home")
		root.geometry("850x454+221+129")
		root.maxsize(1370, 749)
		root.minsize(120, 1)

		
		self.notebook = ttk.Notebook(root)
		
		self.creatCarsTab("  Cars  ")
		self.createCarCategoryTab("  Car category")
		self.createCustomersTab("  Customers")
		self.createTransTab("  Transactions")
		self.createReturnsTab("  Returns")
		self.createBookingTab("  Booking")
		
		self.notebook.pack(fill='both', expand=True, padx=0, pady=0)
		root.focus_set()

	def creatCarsTab(self,text):
		tab = clsTabCars(self.notebook,text)
		
	def createCarCategoryTab(self,text):
		tab = clsTabCategory(self.notebook,text)
	
	def createCustomersTab(self,text):
		tab = clsTabCustomers(self.notebook,text)
	
	def createTransTab(self,text):
		tab = clsTabTransactions(self.notebook,text)
	
	def createBookingTab(self,text):
		tab = clsTabBookings(self.notebook,text)
	def createReturnsTab(self,text):
		tab = clsTabReturns(self.notebook,text) 
	