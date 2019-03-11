import csv
from tkinter import *

def importing_csv_file(filename):
	with open(filename+'.csv') as f:
		reader = csv.reader(f)
		raw_data = [r for r in reader]
	f.close()
	return raw_data[1:]

def add_user(u,p,n,t):
	with open('All_Users.csv', mode='a', newline='') as f:
		writer = csv.writer(f)
		print([u,p,n,t])
		writer.writerow([u,p,n,t])
	f.close()

def get_user_data():
	data = importing_csv_file('All_Users')
	login_info = {}
	for p in data:
		login_info.update({p[0]:p[1]})
	return login_info

def verify(u,p):
	login_info = get_user_data()
	if u in login_info:
		if login_info[u] == p:
			print('Valid Info')

def main(new_mode=False):
	master = Tk()
	master.geometry("250x80")
	master.title("Login")

	if new_mode:
		master.title("Add User")
		master.geometry("270x130")

	Label(master, text="UserName").grid(row=0,columnspan=3)
	Label(master, text="Password").grid(row=1,columnspan = 3)

	if new_mode:
		Label(master, text="Name").grid(row=2,columnspan=3)
		Label(master, text="Student or Lecturer (S/L)").grid(row=3,columnspan = 3)

	password   = StringVar()
	loginKey   = StringVar()
	Users_Name = StringVar()
	s_or_l     = StringVar()

	UserName = Entry(master, textvariable=loginKey)
	passEntry = Entry(master, textvariable=password, show='*')
	UserName.grid(row=0, column=3)
	passEntry.grid(row=1, column=3)

	if new_mode:
		Name = Entry(master, textvariable=Users_Name)
		type_of_user = Entry(master, textvariable=s_or_l)
		Name.grid(row=2,column=3)
		type_of_user.grid(row=3,column=3)

	if not new_mode:
		submit = Button(master, text='Login',command= lambda:verify(loginKey.get(),password.get()))
		submit.grid(row=4,column=2,rowspan = 3)
		new_user = Button(master, text='New User', command=lambda:main(True))
		new_user.grid(row=4)

	if new_mode:
		submit = Button(master, text='Add User',command= lambda:add_user(UserName.get(),passEntry.get(),Name.get(),type_of_user.get()))
		submit.grid(row=4,column=2,rowspan = 3)

	mainloop()



main()