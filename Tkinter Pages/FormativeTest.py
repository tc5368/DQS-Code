from tkinter import *
import tkinter as tk 

test_questions = [ "What is the center most layer of Earth?"]
q_answers = ["Mantle","Inner core","Troposphere","Outer core"]

an = [1]

feedback = ["Read the Geology book"]


def get_test(qu,an):

    v = 0
    l = []
    r = 2
    for x in qu:
        q = Label(window, text = x)
        q.grid(row = 1 , column =0 )
        
        for y in an:
            
            rb = Radiobutton(window, text = y, variable = rv, value= v+1)
            v = v+1
            l.append(rb)
            rb.grid(row = r , column = 0 , sticky = "w")
            r = r+1
        print("  ")
def display ():
    Q_area["text"] = get_test(test_questions, q_answers)

##    def submit():
##
##    def saveAndExit():
##        
##    def mark|():



window = Tk()
window.geometry("800x600")
window.title("Formative Test")

rv = tk.IntVar()

window.columnconfigure(1,weight=1)
window.columnconfigure(3, pad=7)
window.rowconfigure(3, weight= 1)
window.rowconfigure(5, pad =7)


    
label1 = Label(window, text = "Formative Test")
label1.grid(columnspan = 2, sticky = W+E, pady=4, padx=5)

Q_area=Label(window)
Q_area.grid()


##Q_area=Label(window, bg= "blue")
##Q_area.grid(row = 1 , column =0 ,columnspan=3, rowspan = 3, padx = 5, sticky = E+W+S+N)

label3 = Label(window, text = "Attempt../3")
label3.grid(row=1, column=3)
label4 = Label(window, text = "Test ID\n Lecturer\n Module\n Due Date")
label4.grid(row=2, column=3, pady=4)

button1 = Button(window, text="Save and Exit")
button1.grid(row=4, column = 3)
button2 = Button(window, text= "Submit")
button2.grid(row=5,column = 3)
button3 = Button(window, command = display ())
button3.grid()

window.mainloop()
