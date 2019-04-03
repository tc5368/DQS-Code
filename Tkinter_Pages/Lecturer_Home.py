global root
from tkinter import *

from Tkinter_Pages import CreatingTest

def open_create_test_page():
	global root
	root.destroy()
	CreatingTest.main()

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
		Create_Test = Button(self, text='Create Test',command=open_create_test_page)
		Create_Test.grid(row=2,column=17)

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