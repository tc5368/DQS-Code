from tkinter import *
import tkinter as tk
import csv
import os
import random
global root, mark

class FormativeTest(Frame):

	def __init__(self, master, filename):
		Frame.__init__(self, master)
		self.grid()
		self.attempt = 1
		self.attempt_label()
		self.widget()
		self.filename = (str(os.getcwd())+'\\Formulative\\'+filename)
		self.var = {}
		self.select = []
		self.saved_an = []
		self.test()
		self.mark = 0

	def widget(self):
		label1 = Label(self, text = "Formative Test")
		label1.grid(columnspan = 2)
			
		label3 = Label(self, text = "Test ID\n Lecturer\n Module\n Due Date")
		label3.grid(row=2, column=11)

		button1 = Button(self, text="Save and Exit", command = self.save_exit)
		button1.grid(row=4, column = 11)
		button2 = Button(self, text= "Submit", command = self.submit)
		button2.grid(row=5,column = 11)


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

	def checkAnswers(self,final):
		print('Checking Answers')
		index = 0
		correct = []
		Feedback = ''
		with open(self.filename) as csvfile:
			csvread = csv.reader(csvfile)
			next(csvread)
			question = 0
			for line in csvread:
				if self.answers[question] == []:
					print("")

				elif self.answers[question] == '':
					print(line[0]+", you didn't answer this question")
					
				elif line[1] == self.answers[question]:
					print(line[0]+", is correct")
					self.mark += 1
					correct.append(question)
					
				else:
					print(line[0]+", is wrong")
					print(self.attempt)
					if final:
						Feedback += line[-1]+', Correct answer: '+line[1]+'\n'
					else:
						Feedback += line[-1]+'\n'
				question += 1
			messagebox.showinfo('Feedback: ',Feedback)
		return correct
					

	def submit(self):
		global mark, correctly_answerd
		self.attempt_label()
		answers = []
		for i in self.var:
			answers.append(self.var[i].get())
		self.answers = answers

		if self.attempt == 1 or self.attempt == 2:
			self.attempt += 1
			self.attempt_label()
			a = self.checkAnswers(False)
			
		elif self.attempt == 3:
			self.mark = 0
			a = self.checkAnswers(True)
			
			print("Mark: " + str(self.mark))
			mark = self.mark
			correctly_answerd = a 
			exit()	

def exit():
	global root
	root.destroy()

def main(filename):
	global root
	root = Tk()
	root.title("Formative Test")
	root.geometry("800x600")
	app = FormativeTest(root, filename)
	root.mainloop()
	return mark, correctly_answerd