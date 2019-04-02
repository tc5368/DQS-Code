from tkinter import *
import tkinter as tk 
import csv
from tkinter import messagebox

class Questionaire(Frame):

	#Test=["Question","CorrectAns","incorrect","incorrect","incorrect","incorrect","Feedback"]
	pop = []
	Answer_Storage_Temp = []
	PerQuestionStorage = []
	temp = []
	SavingList= []

	def __init__(self, master):
		Frame.__init__(self, master)
		#self.master = master
		self.grid()
		self.Building()

	def Building(self):
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

		question_number_label= StringVar()
		Label(self, textvariable=question_number_label).grid(row=0,column=0,columnspan=1)
		question_number_label.set("Question Number 1")
		Label(self,text ="Answer").grid(row=1,column=0,columnspan=1)
		
		Label(self,text ="Feedback").grid(row=2,column=0,columnspan=1)

		Label(self,text ="The First Answer Inputed Needs To Be The Correct Answer").grid(row=3,column=0,columnspan=1)




	

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
		
		a = self.Answer.get()
		if len(Questionaire.Answer_Storage_Temp) <=4:
			Questionaire.Answer_Storage_Temp.append(a)
			self.Answer.delete(0,END)
			print(Questionaire.Answer_Storage_Temp)
			print(len(Questionaire.Answer_Storage_Temp))
			
		else:
			messagebox.showinfo("Error","Answers are full")

	def Saving(self):
		
		Test = Questionaire.SavingList
		print("Saving")
		with open('Template.csv',mode="a",newline='') as new_file:
			csv_writer = csv.writer(new_file)
			for i in range(len(Test)):
				csv_writer.writerow(Test[i])


#Main
root = Tk()
root.geometry("800x400")
root.title("Create Test Page")
app = Questionaire(root)
root.mainloop()
