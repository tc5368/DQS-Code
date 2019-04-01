
from tkinter import *


class Lecturer_Home(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_Buttons()
		self.create_labels()
		self.create_textboxes()
		self.openSummative()
		self.openFormative()

	def fun_account_options():
		print("")

	def fun_Create_Test():
		print("")

	def fun_Edit_Test():
		print("")

	def fun_View_Formative():
		print("")

	def fun_View_Summative():
		print("")

	def fun_Student_Search():
		print("")

	def create_Buttons(self):
		Account_Options = Button(self, text='Account Options',command=self.fun_account_options)
		Account_Options.grid(row=1,column=17)

		Create_Test = Button(self, text='Create Test',command=self.fun_Create_Test)
		Create_Test.grid(row=2,column=17)

		Edit_Test = Button(self, text='Edit Test',command=self.fun_Edit_Test)
		Edit_Test.grid(row=3,column=17)

		Student_Search = Button(self, text='Student Search',command=self.fun_Student_Search)
		Student_Search.grid(row=4,column=17)

		View_Formative = Button(self, text='View Formative Results',command=self.fun_View_Formative)
		View_Formative.grid(row=5,column=17)

		View_Summative = Button(self, text='View Summative Results',command=self.fun_View_Summative)
		View_Summative.grid(row=6,column=17)

	def create_labels(self):
		Title= StringVar()
		Label(self,textvariable=Title).grid(row=1,column=4)
		Title.set("Title")

		Summative_Tests= StringVar()
		Label(self,textvariable=Summative_Tests).grid(row=5,column=3)
		Summative_Tests.set("Summative Tests Outstanding")

		Formative_Tests= StringVar()
		Label(self,textvariable=Formative_Tests).grid(row=5,column=6)
		Formative_Tests.set("Formative Tests Outstanding")

	def create_textboxes(self):
		print("")

	def openFormative(self):
		t = Text(self)
		t.grid(row=7,column=6,columnspan = 2)
		

	def openSummative(self):
		t = Text(self)
		t.grid(row=7,column=3,columnspan = 2)
		


#Main
root = Tk()
root.geometry("1500x750")
root.title("Lecturer Home")
app = Lecturer_Home(root)
root.mainloop()