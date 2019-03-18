from tkinter import *
import tkinter as tk 
import csv


test_questions = [ "What is the center most layer of Earth?",
                   "The composition of the core of the Earth is thought to be ___","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"]
q_answers = [["Mantle","Inner core","Troposphere","Outer core"],
             ["Basalt","Granite","Peridotite","Solid iron-nickel alloy"],
             ["1","2","3","4"],
             ["1","2","3","4"],
             ["1","2","3","4"],
             ["1","2","3","4"],
             ["1","2","3","4"],
             ["1","2","3","4"],
             ["1","2","3","4"],
             ["1","2","3","4"]]

an = [1,7,8,12,16,20,24,28,32,36]
             


class FormativeTest(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.labels()
        self.buttons()
##        self.scroll = Scrollbar(self)
##        self.scroll.pack(side = RIGHT, fill = Y)
        self.var = IntVar()
        self.get_test(test_questions, q_answers)
        self.attempt = 0
        self.selection = []
        self.counter = 0
        self.feedback = "Read the Geology book"
        

    def buttons(self):
        button1 = Button(self, text="Save and Exit", command =self.save_exit )
        button1.grid(row=4, column = 5)
        button2 = Button(self, text= "Submit", command =self.mark)
        button2.grid(row=5,column = 5)

        
    def labels(self):
        label1 = Label(self, text = "Formative Test")
        label1.grid(columnspan = 2, sticky = W+E)
        label3 = Label(self, text = "Attempt 1/3")
        label3.grid(row=1, column=5)
        label4 = Label(self, text = "Test ID\n Lecturer\n Module\n Due Date")
        label4.grid(row=2, column=5)


    def get_test(self, qu,an):
        
        
        values = list(range(40))
        
        for x in range(len(qu)):
            self.var.set(x)
            q = Label(self, text = qu[x])
            q.grid(column = 0 , sticky = "w")
            
            
            for y in range(4):
                
                rb = Radiobutton(self, text = an[x][y], variable = self.var.get(), value= values[0])
                rb.grid(column = 0 , sticky = "w")
                #print(values[0])
                #print(self.var)
                values.pop(0)


    def save_exit(self):
        sel = 0
        for s in range(10):
            sel = self.var.get()
            self.selection.append(sel)
        print(self.selection)
        self.destroy()
           
        
    def mark(self):
        
        for m in range(10):
            sel = self.var.get()
            if sel == an[m]:
                print("correct")
                self.counter += 1
                
            else:
                print("wronge")

            


        
    def check_an(self):
        for m in range(10):
            sel = self.var.get()
            if sel == an[m]:
                print("correct")
                
            else:
                print("wronge")
                print(self.feedback)




##    def attempt(self):
##        self.attempt+=1
##        self.label3["text"] = "Attempt" + str(self.attempt) + "/3"

        
##    def submit(self):
##        if self.attempt == 3:
##            return 
##        else:
##            return self.check_an()




root = Tk()
root.title("Formative Test")
app = FormativeTest(root)
root.mainloop()



