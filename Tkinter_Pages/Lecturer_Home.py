global root
from tkinter import *

def fun_account_options(value):
	global root, valueG
	valueG = value
	root.destroy()

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

class Lecturer_Home(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_Buttons()
		self.create_labels()
		self.create_textboxes()
		self.openSummative()
		self.openFormative()


	def create_Buttons(self):
		Account_Options = Button(self, text='Account Options',command=lambda:fun_account_options('H'))
		Account_Options.grid(row=1,column=17)

		Create_Test = Button(self, text='Create Test',command=fun_Create_Test)
		Create_Test.grid(row=2,column=17)

		Edit_Test = Button(self, text='Edit Test',command=fun_Edit_Test)
		Edit_Test.grid(row=3,column=17)

		Student_Search = Button(self, text='Student Search',command=fun_Student_Search)
		Student_Search.grid(row=4,column=17)

		View_Formative = Button(self, text='View Formative Results',command=fun_View_Formative)
		View_Formative.grid(row=5,column=17)

		View_Summative = Button(self, text='View Summative Results',command=fun_View_Summative)
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
		


def main():
	global root
	root = Tk()
	root.geometry("1500x750")
	root.title("Lecturer Home")
	app = Lecturer_Home(root)
	root.mainloop()
	return valueG	