#Login.py

from tkinter import * 

def show():
	u = loginKey.get()`
	p = password.get() #get password from entry
	print(u,p)



from tkinter import *

master = Tk()
Label(master, text="UserName").grid(row=0)
Label(master, text="Password").grid(row=1)
password = StringVar() #Password variable
loginKey = StringVar()

UserName = Entry(master, textvariable=loginKey)
passEntry = Entry(master, textvariable=password, show='*')

UserName.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

submit = Button(master, text='Login',command=show)
submit.grid(row=3)
mainloop( )



