#still working on the methods,when i finish i will re-upload the file

from tkinter import *


test_questions = [ "What is the center most layer of Earth?"]

q_answers = ["Mantle","Inner core","Troposphere","Outer core"]

an = [1]

class FormativeTest:
    
    def __init__(self, master):
        self.selected = IntVar()
        self.index = 0
        self.correct = 0
        #
        self.q = self.questions(master, self.index)
        self.c = self.marking(master, 4)
        self.show(self.index)
        
        
    def questions(self, master, index):
        #for q in test_questions:
        q_list = Label(master, text = test_questions[index])
        #r = 1+index
        q_list.grid(row= 1 ,column = 0)
        return q_list
    
##    def questions(file):
##       with open(file ) as csv_file:
##           csv_read =csv.reader(csv_file)
##           next(csv_read)
           
            
                
#
    def choices(self, master, index):
        x = []
        for i in range(index):
            ch = Radiobutton(master, text = "", variable=self.selected, value=i+1)
            x.append(ch)
            ch.grid(row= 3 ,column = 1)
        return x

    def show(sself, index):
        x=0
        self.selected.set(0)
        self.q["text"]= test_questions[index]
        for i in q_answers[index]:
            #
            self.c[x]["text"] = v
            x+=1
        
#    def save_and_exit():
    def marking(self, index):
        if self.selected.get() == a[index]:
            return True
        return False
        
#   def feedback():
        
    def submitting():
        print("Your mark is: ", self.correct, "/", len(test_questions))
##        fi = "dff"
##        feedback = Text(master = window, height=20,width=40).grid()
##        feedback.insert(END, fi)


window = Tk()
window.geometry("400x400")
window.title("Formative Test")


window.columnconfigure(1,weight=1)
window.columnconfigure(3, pad=7)
window.rowconfigure(3, weight= 1)
window.rowconfigure(5, pad =7)

label1 = Label(window, text = "Formative Test")
label1.grid(sticky = W, pady=4,padx=5)

label2 = Label(window, text = "Formative Test")
label2.grid(row=5, sticky = W)

label_Q=Label(window)
label_Q.grid(row = 1 , column =0 ,columnspan=2, rowspan = 4, padx = 5, sticky = E+W+S+N)

label3 = Label(window, text = "Atempt....")
label3.grid(row=1, column=3)
label4 = Label(window, text = "info")
label4.grid(row=2, column=3, pady=4)

button1 = Button(window, text="Save and Exit")
button1.grid(row=5, column = 3)
button2 = Button(window, text= "Submit")
button2.grid(row=7,column = 3)






##topFrame = Frame(window, width=400, height= 100)
##topFrame.grid(row=0)
##
##middleFrame = Frame(window, width=400, height= 200)
##middleFrame.grid(row=1)
##
##bottomFrame = Frame(window, width=400, height= 100)
##bottomFrame.grid(row=2)
##
##
##
##label1 = Label(topFrame, text = "Formative Test")
##label1.grid()
##label2 = Label(middleFrame, text = "Formative Test")
##label2.grid(row=1, column=0)
##
##button1 = Button(bottomFrame, text="Save and Exit")
##button1.grid(row=2, column=0)
##button2 = Button(bottomFrame, text= "Submit")
##button2.grid(row=2, column=3)
##










window.mainloop()




