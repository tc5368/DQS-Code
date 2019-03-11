import subprocess
from tkinter import Tk

window = Tk()
window.geometry("266x208")
window.title("Exam")
window.mainloop()
	
def get_test(file_name):
	file = open(file_name,'r')
	raw = eval(file.read())
	file.close()
	questions = raw[0]; answers = raw[1]
	return questions, answers

def make():
	questions = []
	answers   = []	
	no_qs = int(input('How many questions in the test? '))
	for q in range(1,no_qs+1):
		questions.append(str(input('Q%s>> ' %q)))
		answers.append(str(input('A%s>> ' %q)))
	outString = str(questions) +','+ str(answers)
	file = open('example_test.txt','w')
	file.write(outString)
	file.close

def run():
	files = str(subprocess.check_output('ls'))[2:-1].split('\\r\\n')
	print('There are these current tests in file')
	for f in files:
		if f != '' and f.split('.')[1] != 'py':
			print(f)
	file_name = str(input('Which test do you want to do: '))
	questions, answers = get_test(file_name)
	correct = 0
	for i in range(len(questions)):
		print(questions[i])
		a = str(input('>> '))
		if a == answers[i]:
			print('Correct')
			correct += 1
		else:
			print('Wrong')
	print('Test Complete')
	print('You got %s out of %s' %(correct,len(questions)))
	percentage = str(correct/len(questions)*100)
	print(percentage + '%')

def menu():
	print('Welcome\n')
	print('You can do any of the following options:')
	print('Complete a test with (C)')
	print('Make a new test with (M)')
	print('Get Results for a test with (R)')
	user_choice = str(input('\n>>')).upper()
	if user_choice == 'C':
		run()
	elif user_choice == 'M':
		make()
	elif user_choice == 'R':
		print('getting Results')
		exit()
	else:
		print('invalid')

menu()