from tkinter import *
import tkinter as tk
import csv



class FormativeTest(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.attempt = 1
        self.widget()
        self.var = {}
        self.select = []
        self.saved_an = []
        self.test()
        self.mark = 0
        



    def widget(self):
        label1 = Label(self, text = "Formative Test")
        label1.grid(columnspan = 2)
        
        self.attempt_label()
            
        label3 = Label(self, text = "Test ID\n Lecturer\n Module\n Due Date")
        label3.grid(row=2, column=11)

        button1 = Button(self, text="Save and Exit", command = self.save_exit)
        button1.grid(row=4, column = 11)
        button2 = Button(self, text= "Submit", command = self.submit)
        button2.grid(row=5,column = 11)


    def attempt_label(self):
        
        if self.attempt == 1:
            label2 = Label(self, text = "Attempt 1/3")
            label2.grid(row=1, column=11)
        elif self.attempt == 2:
            label2 = Label(self, text = "Attempt 2/3")
            label2.grid(row=1, column=11)
        else:
            label2 = Label(self, text = "Attempt 3/3")
            label2.grid(row=1, column=11)

    
    def test(self):

        row_n = 2
        index = 0

        with open('q.csv') as csvfile:
            csvread = csv.reader(csvfile)
            next(csvread)
            for line in csvread:
                
                self.var[index] = IntVar()

                label = Label(self, text = line[1])
                label.grid(row = row_n,column = 0, sticky = W)
                
                row_n += 1
                
                radiobutton1 = Radiobutton(self, text = line[2], variable = self.var[index], value = 1, command = self.selection)
                radiobutton1.grid(row = row_n,column = 0)
                radiobutton2 = Radiobutton(self, text = line[3], variable = self.var[index], value = 2, command = self.selection)
                radiobutton2.grid(row = row_n,column = 1)
                radiobutton3 = Radiobutton(self, text = line[4], variable = self.var[index], value = 3, command = self.selection)
                radiobutton3.grid(row = row_n,column = 2)
                radiobutton4 = Radiobutton(self, text = line[5], variable = self.var[index], value = 4, command = self.selection)
                radiobutton4.grid(row = row_n,column = 3)

                row_n += 2
                index += 1




    def selection(self):
        
        choice = 0
        for i in range(10):
            choice = self.var[i].get()
            self.select.append(choice)
        self.saved_an = self.select[-10:]



        
    def save_exit(self):
        
        print(self.saved_an)
        self.destroy()


            
    def checkAnswers(self):

        index = 0
        with open('q.csv') as csvfile:
            csvread = csv.reader(csvfile)
            next(csvread)
            for line in csvread:

                if self.saved_an == []:
                    print("")

                elif self.saved_an[index] == 0:
                    print(line[0]+" you didn't answer this question")

                    
                elif int(line[7]) == self.saved_an[index]:
                    print(line[0]+" is correct")
                    self.mark += 1
                    
                
                    
                else:
                    print(line[0]+" is wrong")
                    
                index +=1

    def submit(self):
        
        
        if self.attempt == 1 or self.attempt == 2:
            self.attempt += 1
            self.checkAnswers()
            
        elif self.attempt == 3:
            self.attempt = 1
            self.mark = 0
            self.checkAnswers()
            
            print("Mark: " + str(self.mark))
        self.attempt_label()
    
        



root = Tk()
root.title("Formative Test")
root.geometry("1200x900")
app = FormativeTest(root)
root.mainloop()


