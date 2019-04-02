from tkinter import *
import os
global results
import csv
class summativeStats(Frame):

	results = []
	def __init__(self,master):
		Frame.__init__(self, master)
		self.grid()
		self.selectTest()
		self.homeButton()
		self.dropdownMenu()

	def homeButton(self):
		#creates a button that allows user to go to the home page
		butHome = Button(self, text = 'Home', font = ('MS', 9, 'bold'), command = self.home) #connect button to home page
		butHome.grid(row=0, column = 0, columnspan = 3)

		#view summative results title
		lblSum = Label(self, text = ' \t View Summative Results', font = ('MS', 14, 'bold'))
		lblSum.grid(row=0, column=4 , columnspan = 6)

	def selectTest(self):
		#global results
		
		
		for file in os.listdir("H:/DQS-Group-Work/DQS-Code/Tkinter_Pages/Formulative"):
			if file.endswith(".csv"):
				summativeStats.results.append(file)
			print(summativeStats.results)

	def home(self):
		print("Conor Was Here")
		with open('Template.csv') as f:
			reader = csv.reader(f)
			for row in reader:
				print(row)
		

	def dropdownMenu(self):
		var = StringVar(root)
		global results

		popupMenu = OptionMenu(self, var, *summativeStats.results)
		popupMenu.grid(row=50, column=50)
		Label(root, text = "Choose a Test to view")

		def change_dropdown(*args):
			#print("Dis")
			#print(var.get())
			#for files in summative.results:
			FileName = str(var.get())
			with open(FileName) as f:
				reader = csv.reader(f)
				for row in reader:
					print(row)
			


		var.trace('w', change_dropdown)





root= Tk()
root.title("Summative Statistic Page")
root.geometry("1100x500")
app = summativeStats(root)

root.mainloop()