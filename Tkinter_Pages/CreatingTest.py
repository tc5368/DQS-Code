
from tkinter import *
import tkinter as tk 
import csv
from tkinter import messagebox
import os

class Questionaire(Frame):

	#Test=["Question","CorrectAns","incorrect","incorrect","incorrect","incorrect","Feedback"]
	pop = []
	Answer_Storage_Temp = []
	PerQuestionStorage = []
	temp = []
	SavingList= []
	TestType = ["S"]

	def __init__(self, master):
		Frame.__init__(self, master)
		#self.master = master
		self.grid()
		self.Building()

	def Building(self):
		TestTypeD = ["S"]
		self.Question = Entry()
		self.Question.grid(row=0,column=1,columnspan=4)

		self.Answer = Entry()
		self.Answer.grid(row=1,column=1,columnspan=4)


		self.Feedback = Entry()
		self.Feedback.grid(row=2,column=1,columnspan=4)

		button1 = Button(self, text="Next Answer", command =self.Next_Answer )
		button1.grid(row=40, column = 40,columnspan=10)

		button2 = Button(self, text= "Next Question", command =self.Next_Question)
		button2.grid(row=41,column = 40,columnspan=10)

		button3 = Button(self, text="Saving", command =self.Saving )
		button3.grid(row=42, column = 40,columnspan=10)

		button3 = Button(self, text="Home", command =self.home )
		button3.grid(row=43, column = 40,columnspan=10)  

		question_number_label= StringVar()
		Label(self, textvariable=question_number_label).grid(row=0,column=0,columnspan=1)
		question_number_label.set("Question Number 1")
		Label(self,text ="Answer").grid(row=1,column=0,columnspan=1)
		
		Label(self,text ="Feedback").grid(row=2,column=0,columnspan=1)

		Label(self,text ="The First Answer Inputed Needs To Be The Correct Answer").grid(row=3,column=0,columnspan=1)
		
		
		i = 0
		while os.path.exists("Summative/TS_%s.csv" % i):
			i += 1
	   

		self.Test_ID= StringVar()
		Label(self,textvariable=self.Test_ID).grid(row=6,column=50)
		self.Test_ID.set("Test ID:"+str(i))

		lecturer= StringVar()
		Label(self,textvariable=lecturer).grid(row=7,column=50)
		lecturer.set("Lecturer Username:"+str(3))

		radiobutton1 = Radiobutton(self, text = "Summative", value = "S", command = self.Sum)
		radiobutton1.grid(row = 65,column = 0)

		radiobutton2 = Radiobutton(self, text = "Formative", value = "F", command = self.Form)
		radiobutton2.grid(row = 65,column = 1)
	def home():
		print("")

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
		
		
		if len(Questionaire.Answer_Storage_Temp) <5:
			messagebox.showinfo("Error","Answer's For This Question Have Not Been Fully Entered")
		elif q == "":
			messagebox.showinfo("Error","The Question Feild Has Not Been Filled Out")
		elif f == "":
			messagebox.showinfo("Error","The Feedback Section Has Not Been Filled Out")
		elif len(Questionaire.SavingList) == 10:
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
			
			print("PerQuestionStorage")
			print(Questionaire.PerQuestionStorage)
			print("SavingList")
			print(Questionaire.SavingList)
			

	def Next_Answer(self):
		#t = Questionaire.Test_ID.get()
		#print(t)
		

		a = self.Answer.get()
		if len(Questionaire.Answer_Storage_Temp) <=4:
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

			fh = open("TS_%s.csv" % i, "w")
			FileName = "TS_%s.csv" % i

			print(FileName)
			Test = Questionaire.SavingList
			print("Saving")
			with open("Formulative%s"%FileName,mode="a",newline='') as new_file:
				csv_writer = csv.writer(new_file)
				for i in range(len(Test)):
					csv_writer.writerow(Test[i])
		elif Questionaire.TestType=="F":
			i = 0
			while os.path.exists("TF_%s.csv" % i):
				i += 1

			fh = open("TF_%s.csv" % i, "w")
			FileName = "TF_%s.csv" % i

			print(FileName)
			Test = Questionaire.SavingList
			print("Saving")
			with open("Formulative%s"%FileName,mode="a",newline='') as new_file:
				csv_writer = csv.writer(new_file)
				for i in range(len(Test)):
					csv_writer.writerow(Test[i])
		else:
			messagebox.showinfo("Error","Please Select A Test Type")
		

		

		




#Main
root = Tk()
root.geometry("800x400")
root.title("Create Test Page")
app = Questionaire(root)
root.mainloop()
