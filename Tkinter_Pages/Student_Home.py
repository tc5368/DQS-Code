from tkinter import *
global test_id, root

def take_example_test():
    global test_id, root
    print('Taking the test.')
    test_id = 'q'
    root.destroy()

class Student_Home(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_Buttons()
        self.create_labels()
        self.create_textboxes()
        self.openSummative()
        self.openFormative()

    def create_Buttons(self):
        Account_Options = Button(self, text='Take Example Test',command=take_example_test)
        Account_Options.grid(row=1,column=11)

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

    def create_textboxes(self):
        print("Put Stuff Here")

    def openFormative(self):
        t = Text(self)
        t.grid(row=7,column=10,columnspan=4,rowspan=2)

    def openSummative(self):
        t = Text(self)
        t.grid(row=7,column=5,columnspan=4,rowspan=2)
        

def main():
    global root
    root = Tk()
    root.geometry("1290x400")
    root.title("Student Home")
    app = Student_Home(root)
    root.mainloop()
    return test_id