from tkinter import *
from tkinter import messagebox
import os
global results
global average
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
		self.createAnotherGraph()
		#self.cleanData()

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
		popupMenu.grid( row=10, column=10)
		lblDropDown = Label(self, text = "Choose a Test to view", font = ('MS', 9, 'bold'))
		lblDropDown.grid( row=9, column=10 )
		self.GraphSome=StringVar()
		Label(root, textvariable=self.GraphSome).grid(row=25,column=25)
		t = Text(self)
		t.grid(row=0,column=0)
		def change_dropdown(*args):
			#print("Dis")
			#print(var.get())
			OnlyOne = False
			count = 1.0
			for files in summativeStats.results:
				self.FileName = str(var.get())
				with open("Summative/%s " %self.FileName) as f:
					reader = csv.reader(f)
					for i in range(0,13):
						next(f)
					reader = csv.reader(f)
					t = Text(self)
					t.grid(row=0,column=0)
						
					if OnlyOne == False:
						t.insert(END,"Student ID Score \n")
						#t.insert(END,"Score")
					for row in reader:
						row.insert(2,"\n")
						count += 1.0
						t.insert(count,' '.join(row))
			self.GraphSome.set(self.FileName)

		var.trace('w', change_dropdown)


	def createGraph(self):

		btnCreateGraph = Button(self, text = 'View All Scores', font = ('MS', 9, 'bold'), command = self.plot_scores)
		btnCreateGraph.grid(row=15, column = 15, columnspan = 3)

	def createAnotherGraph(self):

		btnCreateBar = Button(self, text = 'View Average', font = ('MS', 9, 'bold'), command = self.plot_average)
		btnCreateBar.grid(row=16, column = 15, columnspan = 3)

	def cleanData(self):
		#var = StringVar(root)
		#for files in summativeStats.results:

		#FileName = "Template.csv"#self.GraphSome.get()
		#print(FileName)
		global average
		load =np.loadtxt("Summative/%s" %self.FileName,skiprows=13,dtype=str)
		total = 0
		clean = []
		for e in load:
			a = e.split(',')
			clean.append([a[0],a[1]])
		print(clean)

		for i in clean:
			total += int(i[1])
		print(total)

		average = (total/len(clean))
		return average

	def plot_scores(self, *args):
		load =np.loadtxt("Summative/%s" %self.FileName,skiprows=13,dtype=str)
		total = 0
		clean = []
		studentId = []
		testScore = []
		for e in load:
			a = e.split(',')
			clean.append([a[0],a[1]])
		print(clean)

		for x in clean:
			ident = (x[0])
			score = int(x[1])
			studentId.append(ident)
			testScore.append(score)

		print (self.FileName)
		#index = [1,2,3,4,5]
		#sco = [10,20,30,40,50]
		#plt.bar(self.FileName, average)
		plt.bar(studentId, testScore)
		plt.xlabel('Student ID', fontsize=10)
		plt.xticks(rotation=90)
		plt.ylabel('Score', fontsize=10)
		plt.show()

	def plot_average(self, *args):
		load =np.loadtxt("Summative/%s" %self.FileName,skiprows=13,dtype=str)
		total = 0
		clean = []
		studentId = []
		testScore = []
		for e in load:
			a = e.split(',')
			clean.append([a[0],a[1]])
		print(clean)

		for i in clean:
			total += int(i[1])
		print(total)

		average = (total/len(clean))

		print (self.FileName)

		#plt.bar(self.FileName, average)
		
		plt.bar(self.FileName, average)
		plt.xlabel('Test', fontsize=10)

		plt.ylabel('Average Score', fontsize=10)
		plt.show()
			
				
root= Tk()
root.title("Summative Statistic Page")
root.geometry("600x400")
app = summativeStats(root)
root.mainloop()