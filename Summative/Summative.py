from tkinter import *
import tkinter as tk
import csv
import os
import random
global root, mark
from tkinter import messagebox

class SummativeTest(Frame):

	def __init__(self, master, filename):
		Frame.__init__(self, master)
		self.grid()
		self.attempt = 1
		self.widget()
		self.filename = (str(os.getcwd())+'\\Summative\\'+filename)
		self.var = {}
		self.select = []
		self.saved_an = []
		self.test()
		self.mark = 0

	def widget(self):
		label1 = Label(self, text = "Summative Test")
		label1.grid(columnspan = 2)
		
		self.attempt_label()
			
		label3 = Label(self, text = "Test ID\n Lecturer\n Module\n Due Date")
		label3.grid(row=2, column=11)

		button2 = Button(self, text= "Submit", command = self.submit)
		button2.grid(row=4,column = 11)


	def attempt_label(self):
		if self.attempt == 1:
			label2 = Label(self, text = "Attempt 1/3")
			label2.grid(row=1, column=11)
		elif self.attempt == 2:
			label2 = Label(self, text = "Attempt 2/3")
			label2.grid(row=1, column=11)
		else:
			label2 = Label(self, text = "Attempt 3/3")
			label2.grid(row=1, column=11)

	
	def test(self):
		row_n = 2
		index = 0

		with open(self.filename) as csvfile:
			csvread = csv.reader(csvfile)
			next(csvread)
			for line in csvread:
				if index == 10:
					break
				self.var[index] = StringVar()

				label = Label(self, text = line[0])
				label.grid(row = row_n,column = 0, sticky = W)
				
				row_n += 1
				
				q = [line[1],line[2],line[3],line[4]]
				random.shuffle(q)

				radiobutton1 = Radiobutton(self, text = q[0], variable = self.var[index], value = q[0], command = self.selection)
				radiobutton1.grid(row = row_n,column = 1)
				radiobutton2 = Radiobutton(self, text = q[1], variable = self.var[index], value = q[1], command = self.selection)
				radiobutton2.grid(row = row_n,column = 2)
				radiobutton3 = Radiobutton(self, text = q[2], variable = self.var[index], value = q[2], command = self.selection)
				radiobutton3.grid(row = row_n,column = 3)
				radiobutton4 = Radiobutton(self, text = q[3], variable = self.var[index], value = q[3], command = self.selection)
				radiobutton4.grid(row = row_n,column = 4)

				row_n += 2
				index += 1

	def selection(self):
		None
   
	def save_exit(self):
		print(self.saved_an)
		self.destroy()

	def checkAnswers(self):
		print('Checking Answers')
		with open(self.filename) as csvfile:
			csvread = csv.reader(csvfile)
			next(csvread)
			question = 0
			for line in csvread:
				print(line)
				if question == 10:
					return None
				if self.answers[question] == []:
					print("")

				elif self.answers[question] == '':
					print(line[0]+", you didn't answer this question")
					
				elif line[1] == self.answers[question]:
					print(line[0]+", is correct")
					self.mark += 1
					
				else:
					print(line[0]+", is wrong")
				question += 1
					

	def submit(self):
		global mark
		answers = []
		for i in self.var:
			answers.append(self.var[i].get())
		self.answers = answers
		self.mark = 0
		self.checkAnswers()
		print("Mark: " + str(self.mark))
		mark = self.mark
		exit()	

def exit():
	global root
	messagebox.showinfo("Score:","Well Done You Scored: %s/10" %mark)
	root.destroy()

def main(filename):
	global root
	root = Tk()
	root.title("Summative Test")
	root.geometry("800x600")
	app = SummativeTest(root, filename)
	root.mainloop()
	return mark









