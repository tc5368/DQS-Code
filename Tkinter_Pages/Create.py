from tkinter import *
from tkinter import messagebox
import json
import subprocess

class Questionaire(Frame):

    #Storage For Questions, Answers, Correct Answers and feed back in a list. These are stored so that the lecturer can look at them if they click on the View Questions/Answers/Feedback buttons.
    Question_Storage = ["First Question","Seconds Questions","Third Question"]
    Answer_Storage_Temp = []
    Answer_Storage_Perma = ["Zeroes","First","Second","Third","Fourth","Fith","Sith","Seventh","Eights","Nines","Tens","Evelsisv","Twelves","Thirteens","Fourteenivs"]
    CorrectAnswer_Storage=[4,3,2]
    Feedback_Storage = ["It is Dad","no u","Working?"]
    temp_storage = []
    #Used in the Save and Exit Button, it will save the questions that have been fully completed already into a plain text file
    Questions_Storage_Final = {
    }

    def __init__(self, master):
        #initialise summative class
        Frame.__init__(self, master)
        self.grid()
        self.Create_Buttons()
        self.Create_Labels()
        self.Create_TextBoxes()
       


    #Used in the Next Answer button to cycle through 5 answers for the current question.
    def NextAnswer():
        
        a = Answer.get()

        if len(Answer_Storage_Temp) <=5:
            Answer_Storage_Temp.append(a)
            Answer.delete(0,END)
        else:
            messagebox.showinfo("Error","Answers are full")


    def Save_And_Exit():
            
        for x in range(len(Question_Storage)):

            if x == 0:
                z = x + 0
                f = x + 1
                c = x + 2
                p = x + 3
                q = x + 4
                Questions_Storage_Final[x] = Question_Storage[x],Answer_Storage_Perma[z],Answer_Storage_Perma[f],Answer_Storage_Perma[c],Answer_Storage_Perma[p],Answer_Storage_Perma[q],CorrectAnswer_Storage[x],Feedback_Storage[x]
                
            else:
                f = f + 4
                c = f + 1
                p = c + 1
                q = p + 1
                v = q + 1
                Questions_Storage_Final[x] = Question_Storage[x],Answer_Storage_Perma[f],Answer_Storage_Perma[c],Answer_Storage_Perma[p],Answer_Storage_Perma[q],Answer_Storage_Perma[v],CorrectAnswer_Storage[x],Feedback_Storage[x]
                f = f + 1
            
        with open('file.txt', 'w') as file:
         file.write(json.dumps(Questions_Storage_Final)) 

    def Make_Live():
        messagebox.showinfo("YEET", "I haven't Coded That Option Yet")
            
        

    def Display_Stored_Answers():
        messagebox.showinfo("Answer's Stored",Answer_Storage_Temp)

    def Display_Questions():
        messagebox.showinfo("Question's Stored", Question_Storage)
        #messagebox.showinfo("Answer_Storage_Perma", Answer_Storage_Perma)
        

    def Display_Feedback():
        messagebox.showinfo("Feedback Stored", Feedback_Storage)
        
    def Set_Due_Date():
        print("idk")

    def Load_Saved_Tests():
        print("Error Loading Load_Saved_Tests please try again later after the beep, beep")

    def NextQuestion():
        #Pulls values from the Question, feedback and correct answer textbox
        a = Question.get()
        f = Feedback.get()
        ca = CAnswer.get()
        #Validation
        if len(Question_Storage) == 10:
            messagebox.showinfo("Error", "Ten Questions Have Been Entered In This Test")
        elif len(Answer_Storage_Temp) <=5:
            messagebox.showinfo("Error","Answer's For This Question Have Not Been Fully Entered")
        elif a == "":
            messagebox.showinfo("Error","The Question Feild Has Not Been Filled Out")
        elif f == "":
            messagebox.showinfo("Error","The Feedback Section Has Not Been Filled Out")
        elif ca == "":
            messagebox.showinfo("Error","The Correct Answer Section Has Not Been Filled Out")
        else:
            #Adds the question and feedback to the relevent lists
            Question_Storage.append(a)
            Feedback_Storage.append(f)
            CorrectAnswer_Storage.append(ca)
            Question.delete(0,END)
            CAnswer.delete(0,END)
            Answer.delete(0,END)
            Feedback.delete(0,END)
            if len(Question_Storage) == 0:
                Question_Number = 1
            Question_Number = len(Question_Storage) + 1
            question_number_label.set("Question Number " + str(Question_Number))

            for i in range(len(Answer_Storage_Temp)):
                position = Answer_Storage_Temp[i]
                Answer_Storage_Perma.append(position)
            Answer_Storage_Temp.clear()


            



    
    def Create_Labels(self):
        

        question_number_label= StringVar()
        Label(self, textvariable=question_number_label).grid(row=0)
        question_number_label.set("Question Number 1")
        Label(self,text ="Answer").grid(row=4)
        Label(self,text ="Correct Answer's Number").grid(row=6)
        Label(self,text ="Feedback").grid(row=8)

        Test_ID= StringVar()
        Label(self,textvariable=Test_ID).grid(row=6,column=50)
        Test_ID.set(3)

        lecturer= StringVar()
        Label(self,textvariable=lecturer).grid(row=7,column=50)
        lecturer.set(4)

        Module= StringVar()
        Label(self,textvariable=Module).grid(row=8,column=50)
        Module.set(5)
        #Label(master,textvariable=question_number_label).grid(row=9,column=20)

    def Create_TextBoxes(self):
        Question = StringVar()
        Question = Entry(self, textvariable=Question)
        Question.grid(row=0, column=1)


        CAnswer = StringVar()
        CAnswer = Entry(self, textvariable=CAnswer)
        CAnswer.grid(row=6, column=1)


        Answer = StringVar()
        Answer = Entry(self, textvariable=Answer)
        Answer.grid(row=4, column=1)


        Feedback = StringVar()
        Feedback = Entry(self, textvariable=Feedback)
        Feedback.grid(row=8, column=1)

    def Create_Buttons(self):
        submit_Answer = Button(self, text='Next Answer',command=self.NextAnswer)
        submit_Answer.grid(row=39,column=40)

        submit_NextQuestion = Button(self, text='Next Question',command=self.NextQuestion)
        submit_NextQuestion.grid(row=40,column=40)

        submit_Display_Stored_Answers = Button(self, text='Display Stored Answers',command=self.Display_Stored_Answers)
        submit_Display_Stored_Answers.grid(row=38,column=40)

        submit_Display_Questions = Button(self, text='Display Stored Questions',command=self.Display_Questions)
        submit_Display_Questions.grid(row=37,column=40)

        submit_Display_Feedback = Button(self, text='Display Stored Feedback',command=self.Display_Feedback)
        submit_Display_Feedback.grid(row=36,column=40)

        submit_Save_And_Exit = Button(self, text='Save And Exit',command=self.Save_And_Exit)
        submit_Save_And_Exit.grid(row=35,column=40)

        submit_Make_Live = Button(self, text='Make Live',command=self.Make_Live)
        submit_Make_Live.grid(row=34,column=40)

        submit_Set_Due_Date = Button(self, text='Set_Due_Date',command=self.Set_Due_Date)
        submit_Set_Due_Date.grid(row=33,column=40)

        submit_Load_Saved_Tests = Button(self, text='Load Saved Tests',command=self.Load_Saved_Tests)
        submit_Load_Saved_Tests.grid(row=32,column=40)



    


#Main
root = Tk()
root.geometry("800x400")
root.title("Create Test Page")
app = Questionaire(root)
root.mainloop()