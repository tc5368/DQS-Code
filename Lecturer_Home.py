global root
from tkinter import *
import sumstats
from Formulative import formative_stat_present
import os
import CreatingTest			

def open_create_test_page(u_id):
	global root

	print("open_create_test_page")
	print(u_id)
	root.destroy()
	CreatingTest.main(u_id)
	
	

	root.destroy()
	CreatingTest.main(u_id)


def open_statistics_page():
	global root
	root.destroy()
	formative_stat_present.main()

def open_sum_stats(u_id):
	global root
	root.destroy()
	sumstats.main(u_id)


class Lecturer_Home(Frame):
	results= []
	resultstwo=[]
	def __init__(self,master, user):
		Frame.__init__(self,master)
		self.grid()
		self.user_info = user
		self.create_Buttons()
		self.create_labels()
		self.create_textboxes()
		self.openSummative()
		self.openFormative()


	def create_Buttons(self):
		Create_Test = Button(self, text='Create Test',command=lambda:open_create_test_page(self.user_info))
		Create_Test.grid(row=2,column=17)
		Create_Test = Button(self, text='View Results',command=open_statistics_page)
		Create_Test.grid(row=3,column=17)

		Create_Test = Button(self, text='View Summative Stats',command=lambda:open_sum_stats(self.user_info))
		Create_Test.grid(row=4,column=17)

	def create_labels(self):
		Title= StringVar()
		Label(self,textvariable=Title).grid(row=1,column=4,sticky=N)
		Title.set("Title")

		Summative_Tests= StringVar()
		Label(self,textvariable=Summative_Tests).grid(row=5,column=3,sticky=W)
		Summative_Tests.set("Summative Tests Outstanding")

		Formative_Tests= StringVar()
		Label(self,textvariable=Formative_Tests).grid(row=5,column=6)
		Formative_Tests.set("Formative Tests Outstanding")

	def create_textboxes(self):
		print("")

	def openFormative(self):
		count = 0.0
		for file in os.listdir("Formulative"):
			if file.endswith(".csv"):
				Lecturer_Home.results.append(file)
		tf = Text(self)
		tf.grid(row=7,column=6,sticky=E)

		for files in Lecturer_Home.results:
			print(files)
			count +=1.0
			tf.insert(count,files+'\n')		

	def openSummative(self):
		count = 0.0
		for file in os.listdir("Summative"):
			if file.endswith(".csv"):
				Lecturer_Home.resultstwo.append(file)
		ts = Text(self)
		ts.grid(row=7,column=5,sticky=W)

		for files in Lecturer_Home.resultstwo:
			print(files)
			count +=1.0
			ts.insert(count,files+'\n')

def main(user_info):
	global root
	root = Tk()
	root.geometry("800x600")
	root.title("Lecturer Home")
	app = Lecturer_Home(root,user_info)
	root.mainloop()