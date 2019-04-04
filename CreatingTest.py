global root
from tkinter import *
import tkinter as tk 
import csv, os, Lecturer_Home
from tkinter import messagebox

def home(u):
	global root
	root.destroy()
	Lecturer_Home.main(u)

class Questionaire(Frame):
	pop = []
	Answer_Storage_Temp = []
	PerQuestionStorage = []
	temp = []
	SavingList= [[]]
	TestType = ["S"]

	def __init__(self, master,u_id):
		Frame.__init__(self, master)
		self.user_id = u_id
		self.grid()
		self.Building()
		

	def Building(self):
		TestTypeD = ["S"]
		self.question_number_label= StringVar()
		Label(self, textvariable=self.question_number_label).grid(sticky=W,padx=5)
		self.question_number_label.set("Question Number " +str(len(Questionaire.SavingList)))

		Label(self,text ="Answer").grid(sticky=W,padx=5)
		Label(self,text ="Feedback").grid(sticky=W,padx=5)
		Label(self,text ="The First Answer Inputed Needs To Be The Correct Answer").grid(sticky=W,padx=5)

		self.Question = Entry()
		self.Question.grid(sticky=NW,row=0,column=0,padx=160,pady=5)
		self.Answer = Entry()
		self.Answer.grid(sticky=NW,row=0,column=0,padx=160,pady=35)
		self.Feedback = Entry()
		self.Feedback.grid(sticky=NW,row=0,column=0,padx=160,pady=60)
		self.Answer = Entry()
		self.Answer.grid(sticky=NW,row=0,column=0,padx=160,pady=35)
		
		self.Feedback = Entry()
		self.Feedback.grid(sticky=NW,row=0,column=0,padx=160,pady=60)

		button1 = Button(self, text="Next Answer", command =self.Next_Answer ).grid(sticky=E,row=0,column=3)

		button2 = Button(self, text= "Next Question", command =self.Next_Question).grid(sticky=E,row=1,column=3)

		button3 = Button(self, text="Save", command =self.Saving ).grid(sticky=E,row=2,column=3)


		button4 = Button(self, text="Home", command = lambda:home(self.user_id)).grid(sticky=E,row=3,column=3)
		
		i = 0
		while os.path.exists(str(os.getcwd())+'\\Summative\\'+"TS_%s.csv" % i):
			i += 1

		self.Test_ID= StringVar()
		Label(self,textvariable=self.Test_ID).grid(sticky=NE,row=0,column=4)
		self.Test_ID.set("Test ID:"+str(i))

		lecturer= StringVar()
		Label(self,textvariable=lecturer).grid(sticky=NE,row=1,column=4)
		lecturer.set("Lecturer Username:"+str(self.user_id[0]))
		

		radiobutton1 = Radiobutton(self, text = "Summative", value = "S", command = self.Sum).grid(sticky=SW)

		radiobutton2 = Radiobutton(self, text = "Formative", value = "F", command = self.Form).grid(sticky=SW)
		

	def Sum(self):
		Questionaire.TestType[:]
		Questionaire.TestType = "S"
		i = 0
		while os.path.exists("Summative/TS_%s.csv" % i):
			i += 1
		self.Test_ID.set("Test ID:"+str(i))
		print(Questionaire.TestType)

	def Form(self):
		i = 0
		while os.path.exists("Formulative/TF_%s.csv" % i):
			i += 1
		#self.Test_ID = i
		Questionaire.TestType[:]
		Questionaire.TestType = "F"
		self.Test_ID.set("Test ID:"+str(i))
		print(Questionaire.TestType)

	

	def Next_Question(self):
		q = self.Question.get()
		a = self.Answer.get()
		f = self.Feedback.get()
		
		if len(Questionaire.Answer_Storage_Temp) <4:
			messagebox.showinfo("Error","Answer's For This Question Have Not Been Fully Entered")
		elif q == "":
			messagebox.showinfo("Error","The Question Feild Has Not Been Filled Out")
		elif f == "":
			messagebox.showinfo("Error","The Feedback Section Has Not Been Filled Out")
		elif len(Questionaire.SavingList) == 11:
			messagebox.showinfo("Error","10 Questions Have Already Been Entered In This Test")
		else:
			Questionaire.PerQuestionStorage.append(q)

			for i in range(len(Questionaire.Answer_Storage_Temp)):
				position = Questionaire.Answer_Storage_Temp[i]
				Questionaire.PerQuestionStorage.append(position)
			del Questionaire.Answer_Storage_Temp[:]

			Questionaire.PerQuestionStorage.append(f)
			self.Question.delete(0,END)
			self.Answer.delete(0,END)
			self.Feedback.delete(0,END)

			new_list = Questionaire.PerQuestionStorage.copy()
			del Questionaire.PerQuestionStorage[:]
			Questionaire.SavingList.append(new_list)
			self.question_number_label.set("Question Number " +str(len(Questionaire.SavingList)))

			print("PerQuestionStorage")
			print(Questionaire.PerQuestionStorage)
			print("SavingList")
			print(Questionaire.SavingList)
			

	def Next_Answer(self):
		a = self.Answer.get()
		if len(Questionaire.Answer_Storage_Temp) <=3:
			Questionaire.Answer_Storage_Temp.append(a)
			self.Answer.delete(0,END)
			print(Questionaire.Answer_Storage_Temp)
			print(len(Questionaire.Answer_Storage_Temp))
			
		else:
			messagebox.showinfo("Error","Answers are full")

	def Saving(self):
		if Questionaire.TestType=="S":
			i = 0
			while os.path.exists("TS_%s.csv" % i):
				i += 1

			fh = open(str(os.getcwd())+'\\Summative\\'+"TS_%s.csv" % i, "w")
			filename = "TS_%s.csv" % i

			print(filename)
			Test = Questionaire.SavingList
			print("Saving")
			with open(str(os.getcwd())+'\\Summative\\'+filename,mode="a",newline='') as new_file:
				csv_writer = csv.writer(new_file)
				for i in range(len(Test)):
					csv_writer.writerow(Test[i])
		elif Questionaire.TestType=="F":
			i = 0
			while os.path.exists(str(os.getcwd())+'\\Formulative\\'+"TF_%s.csv" % i):
				i += 1

			fh = open(str(os.getcwd())+'\\Formulative\\'+"TF_%s.csv" % i, "w")
			filename = "TF_%s.csv" % i

			print(filename)
			Test = Questionaire.SavingList
			print("Saving")
			with open(str(os.getcwd())+'\\Formulative\\'+filename,mode="a",newline='') as new_file:
				csv_writer = csv.writer(new_file)
				for i in range(len(Test)):
					csv_writer.writerow(Test[i])
		else:
			messagebox.showinfo("Error","Please Select A Test Type")

def main(u_id):
	global root
	root = Tk()
	root.geometry("600x400")
	root.title("Create Test Page")
	app = Questionaire(root,u_id)
	root.mainloop()
