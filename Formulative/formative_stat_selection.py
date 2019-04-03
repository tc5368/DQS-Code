from tkinter import *
global root,sel
import Lecturer_Home

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
    def __init__(self, master):
        # Initialise Formative Stats class
        
        Frame.__init__(self, master)
        self.grid()
        self.introLabel()
        self.searches()
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

        #e1 = Entry(self)
        #e1.grid(row=1, column=1)

        Button(self, text='Search Test', fg = "black", bg= "white", font = "Helvetica 18 bold").grid(row=1, column=3, sticky=W, padx=10, pady=10)
        Button(self, text='Home',command=home, fg = "black", bg= "white", font = "Helvetica 18 bold").grid(row=2, column=3, sticky=W, padx=10, pady=10)


    def testList(self):
        listbox = Listbox(self)
        listbox.grid(row=2, column=1)
        
        test = {1:["Template", ":Computing"], 2:[113, ":History"], 3:[114, ":Maths"], 4:[115, ":English"]}
        for key in test:
            
            value = test.get(key)
            listbox.insert(END, value)

        # this function is called when the selection in the listbox changes   
        #def showSelection(*args):
            #chosenTestList = listbox.curselection()
            #if len(chosenTestList)==1:
                #chosenTestID = int(chosenTestList[0])
                #listbox.see(chosenTestID)
                #testType = tests[chosenTestID]
                #statusmsg.set("the test type is: ", testType)

        def CurSelect(evt):
            sel((listbox.get(listbox.curselection()))[0])

            
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
