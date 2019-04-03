<<<<<<< HEAD
from tkinter import *
from tkinter import messagebox
import os
global results
import csv
import matplotlib.pyplot as plt
import numpy as np

class summativeStats(Frame):
#IMPORTANT COMMENT LINE 62
	results = []
	def __init__(self,master):
		Frame.__init__(self, master)
		self.grid()
		self.selectTest()
		self.homeButton()
		self.dropdownMenu()
		self.createGraph()

	def homeButton(self):
		#creates a button that allows user to go to the home page
		butHome = Button(self, text = 'Home', font = ('MS', 9, 'bold')) #connect button to home page
		butHome.grid(row=0, column = 0, columnspan = 3)

		#view summative results title
		lblSum = Label(self, text = ' \t View Summative Results', font = ('MS', 14, 'bold'))
		lblSum.grid(row=0, column=4 , columnspan = 6)


#LINE 62 DONT FORGET UR COMMENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def selectTest(self):
		#global results
		
		for file in os.listdir("Summative"):
			if file.endswith(".csv"):
				summativeStats.results.append(file)
			print(summativeStats.results)

	def home(self):
		print("Conor Was Here")
		
		

	def dropdownMenu(self):
		var = StringVar(root)
		global results

		popupMenu = OptionMenu(self, var, *summativeStats.results)
		popupMenu.grid(row=50, column=50)
		Label(root, text = "Choose a Test to view")
		self.GraphSome=StringVar()
		Label(root, textvariable=self.GraphSome).grid(row=25,column=25)
		self.GraphSome.set("The Current Test Being Displayed Is: " )
		def change_dropdown(*args):
			#print("Dis")
			#print(var.get())
			
			for files in summativeStats.results:
				self.FileName = str(var.get())
				with open("Summative/%s " %self.FileName) as f:
					reader = csv.reader(f)
					for i in range(0,13):
						next(f)
					reader = csv.reader(f)
					t = Text(self)
					t.grid(row=0,column=0)
					for row in reader:
						popop = row.insert(7,"\n")         # IMPORTANT change to 2 for student id and test score
						t.insert(1.0,' '.join(row))
			self.GraphSome.set(self.FileName)

		var.trace('w', change_dropdown)


	def createGraph(self):

		"""btnCreateGraph = Button(self, text = 'Create a Graph', font = ('MS', 9, 'bold'), command = self.plot_average)
								btnCreateGraph.grid(row=55, column = 50, columnspan = 3)"""

	def cleanData(self):
		#var = StringVar(root)
		#for files in summativeStats.results:

		#FileName = "Template.csv"#self.GraphSome.get()
		#print(FileName)
		load =np.loadtxt("Summative/%s" % self.FileName,skiprows=13,dtype=str)
		total = 0
		clean = []
		for e in load:
			a = e.split(',')
			clean.append([a[0],a[1]])
		print(clean)

		for i in clean:
			total += int(i[1])
		print(total)

		self.average = (total/len(clean))

	"""def plot_average():
		index = [1,2,3,4,5]
		sco = [10,20,30,40,50]
		plt.bar(index, sco)
	    plt.xlabel('Student Number', fontsize=5)
	    plt.ylabel('Score', fontsize=5)
	    plt.xticks(index, label, fontsize=5, rotation=30)
	    plt.show() """

						
root= Tk()
root.title("Summative Statistic Page")
root.geometry("1100x500")
app = summativeStats(root)

=======
from tkinter import *
from tkinter import messagebox
import os
global results
import csv
import matplotlib.pyplot as plt
import numpy as np

class summativeStats(Frame):
#IMPORTANT COMMENT LINE 62
	results = []
	def __init__(self,master):
		Frame.__init__(self, master)
		self.grid()
		self.selectTest()
		self.homeButton()
		self.dropdownMenu()
		self.createGraph()

	def homeButton(self):
		#creates a button that allows user to go to the home page
		butHome = Button(self, text = 'Home', font = ('MS', 9, 'bold')) #connect button to home page
		butHome.grid(row=0, column = 0, columnspan = 3)

		#view summative results title
		lblSum = Label(self, text = ' \t View Summative Results', font = ('MS', 14, 'bold'))
		lblSum.grid(row=0, column=4 , columnspan = 6)


#LINE 62 DONT FORGET UR COMMENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def selectTest(self):
		#global results
		
		for file in os.listdir("Summative"):
			if file.endswith(".csv"):
				summativeStats.results.append(file)
			print(summativeStats.results)

	def home(self):
		print("Conor Was Here")
		
		

	def dropdownMenu(self):
		var = StringVar(root)
		global results

		popupMenu = OptionMenu(self, var, *summativeStats.results)
		popupMenu.grid(row=50, column=50)
		Label(root, text = "Choose a Test to view")
		self.GraphSome=StringVar()
		Label(root, textvariable=self.GraphSome).grid(row=25,column=25)
		self.GraphSome.set("The Current Test Being Displayed Is: " )
		def change_dropdown(*args):
			#print("Dis")
			#print(var.get())
			
			for files in summativeStats.results:
				self.FileName = str(var.get())
				with open("Summative/%s " %self.FileName) as f:
					reader = csv.reader(f)
					for i in range(0,13):
						next(f)
					reader = csv.reader(f)
					t = Text(self)
					t.grid(row=0,column=0)
					for row in reader:
						popop = row.insert(7,"\n")         # IMPORTANT change to 2 for student id and test score
						t.insert(1.0,' '.join(row))
			self.GraphSome.set(self.FileName)

		var.trace('w', change_dropdown)


	def createGraph(self):

		"""btnCreateGraph = Button(self, text = 'Create a Graph', font = ('MS', 9, 'bold'), command = self.plot_average)
								btnCreateGraph.grid(row=55, column = 50, columnspan = 3)"""

	def cleanData(self):
		#var = StringVar(root)
		#for files in summativeStats.results:

		#FileName = "Template.csv"#self.GraphSome.get()
		#print(FileName)
		load =np.loadtxt("Summative/%s" % self.FileName,skiprows=13,dtype=str)
		total = 0
		clean = []
		for e in load:
			a = e.split(',')
			clean.append([a[0],a[1]])
		print(clean)

		for i in clean:
			total += int(i[1])
		print(total)

		self.average = (total/len(clean))

	"""def plot_average():
		index = [1,2,3,4,5]
		sco = [10,20,30,40,50]
		plt.bar(index, sco)
	    plt.xlabel('Student Number', fontsize=5)
	    plt.ylabel('Score', fontsize=5)
	    plt.xticks(index, label, fontsize=5, rotation=30)
	    plt.show() """

						
root= Tk()
root.title("Summative Statistic Page")
root.geometry("1100x500")
app = summativeStats(root)

>>>>>>> 94dea6485f7a2b105f472873163f271d7adc629f
root.mainloop()