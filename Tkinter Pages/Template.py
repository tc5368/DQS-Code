
from tkinter import *


class template(frame):
	def __init__(self,master):
		frame.__init__(self,master)
		self.grid()
		self.create_Buttons()
        self.create_labels()
        self.create_textboxes()

	def create_Buttons():
		Account_Options = Button(self, text='Account Options',command=self.account_options_fun)
        Account_Options.grid(row=1,column=11)


	def create_labels():
		Title= StringVar()
        Label(self,textvariable=Title).grid(row=1,column=7)
        Title.set("Title")

	def create_textboxes():
		Question = StringVar()
        Question = Entry(self, textvariable=Question)
        Question.grid(row=0, column=1)


#Main
root = Tk()
root.geometry("800x400")
root.title("template")
app = template(root)
root.mainloop()