from tkinter import *
#from home page import *

class viewSummative(Frame):
	#GUI Setup

	def __init__(self, master):
		#initialise summative class
		Frame.__init__(self, master)
		self.grid()
		self.homeButton()
		self.searchStudent()
		self.viewAll()
		#self.showResults()
		self.openResults()
		
	def homeButton(self):
		#creates a button that allows user to go to the home page
		butHome = Button(self, text = 'Home', font = ('MS', 9, 'bold')) #connect button to home page frame
		butHome.grid(row=0, column = 0, columnspan = 3)

		#view summative results title
		lblSum = Label(self, text = ' \t View Summative Results', font = ('MS', 14, 'bold'))
		lblSum.grid(row=0, column=4 , columnspan = 6)

	def searchStudent(self):
		#creates a title, field to input student ID and search student

		lblUser = Label(self, text = 'User ID:' , font = ('MS', 9, 'bold'))
		lblUser.grid(row = 5, column = 0, columnspan = 2)

		#field to input data
		self.entID = Entry(self)
		self.entID.grid(row = 5, column = 3, columnspan = 5)

		#search button
		butSearch = Button(self, text = 'Search', font = ('MS', 9, 'bold'))
		butSearch.grid(row = 5, column = 8, columnspan = 2 )

	def viewAll(self):
		#t1 = Toplevel(root)
		#Trial(t1)

		butView = Button(self, text = "View All Students", font = ('MS', 9, ' bold'))
		butView.grid(row = 5, column = 11, rowspan = 2, columnspan = 2)


	def openResults(self):
		t = Text(self)
		t.grid(row = 10, column = 0, columnspan = 20)
		f = open('Results.txt')
		t.insert(1.0, f.read())



# Main
root = Tk()
root.geometry("800x600")
root.title("View Summative Results")
app = viewSummative(root)
root.mainloop()




