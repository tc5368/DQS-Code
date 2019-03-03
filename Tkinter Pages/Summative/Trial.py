from Tkinter import *

def showStudent():
	pass

root = Tk()
text = Text(root)
text.insert(INSERT, "User ID \t \t")
text.config(state = DISABLED)
text.config(state = 'normal')
text.insert(INSERT, "Test ID \t \t")
text.config(state = DISABLED)
text.config(state = 'normal')
text.insert(END, "Total Mark \t \t")
text.config(state = DISABLED)
text.config(state = 'normal')
text.insert(END, "X Results \t \t")
text.config(state = DISABLED)
text.config(state = 'normal')
text.insert(END, "Y Results \t \t")
text.config(state = DISABLED)

text.pack()
root.mainloop()