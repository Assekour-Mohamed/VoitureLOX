import tkinter as tk

from admin import clsAdmin
from winAdminHome import clsAdminHome
from tkinter import messagebox
import loginInfo
class clsWinLogin:
	def __init__(self,root) :	
		self.root = root
		root.configure(background="#002953")
		root.title("addmin home")
		root.geometry("742x454+421+129")
		root.maxsize(1370, 749)
		root.minsize(120, 1)

		# Create frame for admin login
		namespace = tk.Frame(root, borderwidth=2, background="#C0C0C0", height=235, highlightbackground="#d9d9d9", highlightcolor="#000000", width=335)
		namespace.place(relx=0.283, rely=0.289, relwidth=0.451, relheight=0.522)

		# Create widgets for admin login
		Label2 = tk.Label(namespace, text="Admin Info:", font="-family {Cascadia Mono} -size 12", background="#C0C0C0", foreground="#000000")
		Label2.place(relx=0.328, rely=0.043)
		Label2_1 = tk.Label(namespace, text="Username (ID):", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2_1.place(relx=0.09, rely=0.213)
		Label2_1_1 = tk.Label(namespace, text="Password:", font="-family {Cascadia Mono} -size 10", background="#C0C0C0", foreground="#000000")
		Label2_1_1.place(relx=0.09, rely=0.511)
		self.enUserID = tk.Entry(namespace, background="white", font="-family {Courier New} -size 10", foreground="#000000")
		self.enUserID.place(relx=0.09, rely=0.34, relwidth=0.82, relheight=0.13)
		self.enPwd = tk.Entry(namespace, background="white", font="-family {Courier New} -size 10", foreground="#000000", show="*")
		self.enPwd.place(relx=0.09, rely=0.596, relwidth=0.82, relheight=0.13)
		self.btnAdminLogin = tk.Button(namespace, text="Log in", font="-family {Cascadia Mono} -size 12 -weight bold", command= self.adimnLogin)
		self.btnAdminLogin.place(relx=0.428, rely=0.766)

		# Create button for customer login
		self.btnCustLogin = tk.Button(root, text="Log in as customer", font="-family {Cascadia Mono} -size 12 -weight bold", command=self.customerLogin)
		self.btnCustLogin.place(relx=0.283, rely=0.859, relwidth=0.451)

		# Create label for login window
		Label1 = tk.Label(root, text="LOGIN WINDOW", font="-family {Cascadia Mono} -size 16 -weight bold", background="#C0C0C0", foreground="#000000")
		Label1.place(relx=0, rely=0.067, relwidth=1, relheight=0.136)
		root.focus_set()
	
		admin = clsAdmin.EmptyadminObject(loginInfo.DB_Mang)
	def adimnLogin(self):
	
		id = self.enUserID.get()
		pwd = self.enPwd.get()

		clsWinLogin.admin = clsWinLogin.admin.searchadminInfoInadminsTaleByIDandPassword(id,pwd)
		
		if clsWinLogin.admin :
			self.showAdminHomeWindow()
		else :
			messagebox.showinfo("Log in info", "wrong Usename or password!!!")

		loginInfo.DB_Mang.close_connection()
	
	def showAdminHomeWindow(self):
		
		self.root.destroy()
		root = tk.Tk()
		home = clsAdminHome(root)
		
		root.mainloop()
    


	def customerLogin():
		pass
	 


