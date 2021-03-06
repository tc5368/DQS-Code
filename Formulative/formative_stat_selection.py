from tkinter import *
global root,sel
import Lecturer_Home
import os

def sel(value):
    global root, sel
    sel = value
    root.destroy()

def home():
    global root
    root.destroy()
    Lecturer_Home.main()

class FormativeStats(Frame):
    # GUI Setup
    results=[]
    def __init__(self, master):
        # Initialise Formative Stats class
        
        Frame.__init__(self, master)
        self.grid()
        self.introLabel()
        self.searches()
        self.openFormative()
        self.testList()
        

    def introLabel(self):
        introLabel = Label(self, 
                     text="Formative Statistics Page",
                     fg = "black",
                     bg = "light grey",
                     font = "Helvetica 24 bold italic").grid(row=0, column=1, padx=200, pady=20)

    def searches(self):
        
        searchLabel = Label(self, text="Test ID", font= "Helvetica 18 bold")
        searchLabel.grid(row=1, column=1)

        Button(self, text='Home',command=home, fg = "black", bg= "white", font = "Helvetica 18 bold").grid(row=2, column=3, sticky=W, padx=10, pady=10)

    def openFormative(self):
        
        count = 0.0
        for file in os.listdir("Formulative"):
            if file.endswith(".csv"):
                FormativeStats.results.append(file)
        


    def testList(self):
        listbox = Listbox(self)
        listbox.grid(row=2, column=1)
        test = FormativeStats.results 
        for key in range(len(test)):
            
            value = test[key]
            listbox.insert(END, value)
            
        def CurSelect(evt):
            sel((listbox.get(listbox.curselection())))

            
        listbox.bind('<<ListboxSelect>>',CurSelect)
            
        
        def check_index(element):
           try:
               index = listbox.get(0, "end").index(element)
               return index
           except:
               #print('Item can not be found in the list!')
               #index = -1 
               #return index
                None

# Main
def main():
    global root
    root = Tk()
    root.title("Formative Statistic Page")
    root.geometry("1100x500")
    root.resizable(0, 0)
    app = FormativeStats(root)

    root.mainloop()
    return sel