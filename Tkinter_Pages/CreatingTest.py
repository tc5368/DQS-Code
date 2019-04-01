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
		self.labels()
		self.Textboxes()
		self.buttons()

	def Textboxes(self):
		self.Question = Entry()
		self.Question.grid(row=0,column=2)

		self.Answer = Entry()
		self.Answer.grid(row=4,column=2)

		#self.CorrectAns = Entry()
		#self.CorrectAns.grid(row=6,column=2)

		self.Feedback = Entry()
		self.Feedback.grid(row=8,column=2)  

	def buttons(self):
		button1 = Button(self, text="Next Answer", command =self.Next_Answer )
		button1.grid(row=40, column = 40)

		button2 = Button(self, text= "Next Question", command =self.Next_Question)
		button2.grid(row=41,column = 40)

		button3 = Button(self, text="Saving", command =self.Saving )
		button3.grid(row=42, column = 40)

	def labels(self):
		question_number_label= StringVar()
		Label(self, textvariable=question_number_label).grid(row=0)
		question_number_label.set("Question Number 1")
		Label(self,text ="Answer").grid(row=4)
		#Label(self,text ="Correct Answer's Number").grid(row=6)
		Label(self,text ="Feedback").grid(row=8)


	

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
		else:
			Questionaire.PerQuestionStorage.append(q)

			for i in range(len(Questionaire.Answer_Storage_Temp)):
				position = Questionaire.Answer_Storage_Temp[i]
				Questionaire.PerQuestionStorage.append(position)
			del Questionaire.Answer_Storage_Temp[:]


			#Questionaire.PerQuestionStorage.extend(Questionaire.Answer_Storage_Temp)
			Questionaire.PerQuestionStorage.append(f)
			self.Question.delete(0,END)
			self.Answer.delete(0,END)
			self.Feedback.delete(0,END)
			#Questionaire.Answer_Storage_Temp.clear()
			print("BeforePerQuestionStorage")
			print(Questionaire.PerQuestionStorage)

			"""for x in range(len(Questionaire.PerQuestionStorage)):
													positiontwo = Questionaire.PerQuestionStorage[x]
													Questionaire.SavingList.append(positiontwo)
												del Questionaire.PerQuestionStorage[:]"""

			Questionaire.SavingList.append(Questionaire.PerQuestionStorage)
			#Questionaire.SavingList.append(Questionaire.PerQuestionStorage)
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
		#Test=["Question","CorrectAns","incorrect","incorrect","incorrect","incorrect","Feedback"]
		Test = Questionaire.SavingList
		print("Saving")
		with open('Template.csv',mode="a",newline='') as new_file:
			csv_writer = csv.writer(new_file)
			for i in range(len(Test)):
				csv_writer.writerow(Test)


#Main
root = Tk()
root.geometry("800x400")
root.title("Create Test Page")
app = Questionaire(root)
root.mainloop()
