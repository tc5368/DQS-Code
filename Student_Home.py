from tkinter import *
global test_id, root
import os, csv

def test_selected(test_name):
    global root, test_id
    test_id = test_name
    root.destroy()


class Student_Home(Frame):
    SummativeResults=[]
    FormativeResults=[]

    def __init__(self,master,user_id):
        Frame.__init__(self,master)
        self.u = user_id
        self.grid()
        self.create_Buttons()
        self.create_labels()
        self.openTests()
        self.selectTest()


    def openTests(self):
        
        for file in os.listdir("Summative"):
            if file.endswith(".csv"):
                Student_Home.SummativeResults.append(file)
                
        for filetwo in os.listdir("Formulative"):
            if filetwo.endswith(".csv"):
                Student_Home.FormativeResults.append(filetwo)

    def create_Buttons(self):
        Select_test = Button(self, text='Submit',command=lambda:test_selected())
        Select_test.grid(row=1,column=12)

    def create_labels(self):

        Summative_Tests= StringVar()
        Label(self,textvariable=Summative_Tests).grid(row=6,column=5)
        Summative_Tests.set("Summative Tests To Take")

        Formative_Tests= StringVar()
        Label(self,textvariable=Formative_Tests).grid(row=6,column=10)
        Formative_Tests.set("Formative_Tests Tests To Take")

    def selectTest(self):
        self.var = StringVar(root)
        for i in Student_Home.SummativeResults:
            dontshow = []
            with open((str(os.getcwd())+'\\Summative\\'+i)) as csvfile:
                csvread = csv.reader(csvfile)
                for line in csvread:
                    if line == []:
                        continue
                    else:
                        dontshow.append(line[0])
            if self.u not in dontshow :               
                popupMenu = OptionMenu(self, self.var, *Student_Home.SummativeResults)
                popupMenu.grid(row=5, column=6)

        print(self.var.get())
        self.vartwo = StringVar(root)
        for i in Student_Home.FormativeResults:
            dontshow = []
            with open((str(os.getcwd())+'\\Formulative\\'+i)) as csvfile:
                csvread = csv.reader(csvfile)
                for line in csvread:
                    if line == []:
                        continue
                    else:
                        dontshow.append(line[0])
            if self.u not in dontshow :          
                popupMenutwo = OptionMenu(self, self.vartwo, *Student_Home.FormativeResults)
                popupMenutwo.grid(row=5, column=7)

        def ReturningTestType(*args):
            test_selected(self.var.get())
            
        def ReturningTestTypetwo(*args):
            test_selected(self.vartwo.get())

        self.var.trace('w', ReturningTestType)
        self.vartwo.trace('w', ReturningTestTypetwo)
        
        
        

def main(user_id):
    global root
    root = Tk()
    root.geometry("800x600")
    root.title("Student Home")
    app = Student_Home(root,user_id)
    root.mainloop()
    return test_id