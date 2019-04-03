from tkinter import *
global test_id, root
import os
def take_example_test():
    global test_id, root
    print('Taking the test.')
    test_id = 'q'
    root.destroy()

def test_selected(test_name):
    global root, test_id
    test_id = test_name
    root.destroy()

class Student_Home(Frame):
    SummativeResults=[]
    FormativeResults=[]

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_Buttons()
        self.create_labels()
        self.openTests()
        self.selectTest()
        

    def openTests(self):
        #global results
        
        for file in os.listdir("Summative"):
            if file.endswith(".csv"):
                Student_Home.SummativeResults.append(file)
            #print(Student_Home.SummativeResults)
                
        for filetwo in os.listdir("Formulative"):
            if filetwo.endswith(".csv"):
                Student_Home.FormativeResults.append(filetwo)
            #print(Student_Home.FormativeResults)

    def create_Buttons(self):
        Template_test = Button(self, text='Take Example Test',command=take_example_test)
        Template_test.grid(row=1,column=11)
        Select_test = Button(self, text='Submit',command=lambda:test_selected())
        Select_test.grid(row=1,column=12)

    def create_labels(self):
        Title= StringVar()
        Label(self,textvariable=Title).grid(row=1,column=7)
        Title.set("Title")

        Summative_Tests= StringVar()
        Label(self,textvariable=Summative_Tests).grid(row=6,column=5)
        Summative_Tests.set("Summative Tests To Take")

        Formative_Tests= StringVar()
        Label(self,textvariable=Formative_Tests).grid(row=6,column=10)
        Formative_Tests.set("Formative_Tests Tests To Take")

    def selectTest(self):
        self.var = StringVar(root)
        #global SummativeResults
        popupMenu = OptionMenu(self, self.var, *Student_Home.SummativeResults)
        popupMenu.grid(row=5, column=6)

        print(self.var.get())
        self.vartwo = StringVar(root)
        #global SummativeResults
        popupMenutwo = OptionMenu(self, self.vartwo, *Student_Home.FormativeResults)
        popupMenutwo.grid(row=5, column=7)

        def ReturningTestType(*args):
            test_selected(self.var.get())

        def ReturningTestTypetwo(*args):
            test_selected(self.vartwo.get())

        self.var.trace('w', ReturningTestType)
        self.vartwo.trace('w', ReturningTestTypetwo)
        
        
        

def main():
    global root
    root = Tk()
    root.geometry("1290x400")
    root.title("Student Home")
    app = Student_Home(root)
    root.mainloop()
    return test_id