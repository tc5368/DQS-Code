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

	"""def showResults(self):

		lblUserID = Label(self, text = 'User ID:', font = ('MS', 9, 'bold'))
		lblUserID.grid(row = 7, column = 0, columnspan = 5)

		lblTestID = Label(self, text = 'Test ID:', font = ('MS', 9, 'bold'))
		lblTestID.grid(row = 7, column = 4, columnspan = 4)

		lblTestResults = Label(self, text = 'Test Results:', font = ('MS', 9, 'bold'))
		lblTestResults.grid(row = 7, column = 8, columnspan = 3)

		lblTestResultsX = Label(self, text = 'Test Results X:', font = ('MS', 9, 'bold'))
		lblTestResultsX.grid(row = 7, column = 12 , columnspan = 3)

		lblTestResultsY = Label(self, text = 'Test Results X:', font = ('MS', 9, 'bold'))
		lblTestResultsY.grid(row = 7, column = 20, columnspan = 5) """

	def openResults(self):
		t = Text(self)
		t.grid(row = 10, column = 0, columnspan = 20)
		f = open('Results.txt')
		t.insert(1.0, f.read())



# Main
root = Tk()
root.title("View Summative Results")
app = viewSummative(root)
root.mainloop()


"""def presentResults(self):
		#text field to display all the results

		T = Text(root, height = 30, width = 30)
		T.pack()
		T.insert(END, "User ID" + "\t" + "\t" + "Text ID")
		///new file///
		class displayResult(Frame):
	#setting up the new GUI
	def __init__(self, master):

		Frame.__init__(self, master)
		self.pack()
		self.retrieveResults()

	def retrieveResults(self):


		import shelve
		db = shelve.open('resultsdb')
		respNo = len(db)

		for i in range(1, respNo):
			Ans = get.db(str(i))

		db.close

		self.txtDisplay = Text(self, height = 14, width = 85)
		self.txtDisplay.tag_configure('boldfont', font = ('MS', 8, 'bold'))
		self.txtDisplay.tag_configure('normfont', font = ('MS', 8))

		tabResults = ""
		tabResults += ("\t" + "\t" + "\t")
		self.txtDisplay.insert(END, "User ID" + tabResults + "Test ID" + tabResults + "Total Score" + "\t" + "x" + "\t" + "y")
		#self.txtDisplay.insert(END other stuff)

		self.txtDisplay.pack()
		
	root = Tk()
	root.title("Summative Results")
	app = (root)
	root.mainloop() """




