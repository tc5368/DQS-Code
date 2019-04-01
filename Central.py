from User_Info import login as lg
import Tkinter_pages.Student_Home.py

print('Logging in now')
user_id = lg.main()
print('Sucsessfully logged in %s' %user_id)

user_info = lg.importing_csv_file('User_Info/All_Users')
print('Getting Info')
def get_info():
	for e in user_info:
		if e[0] == user_id: return e
user_info = get_info()
print('Succsesfully found info: ',user_info)

