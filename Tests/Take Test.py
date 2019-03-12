import csv
from random import randint as r

def get_scores(filename):
	with open(filename+'.csv') as f:
		reader = csv.reader(f)
		raw_data = [r for r in reader]
	f.close()
	return raw_data[11:]

def get_questions(filename):
	with open(filename+'.csv') as f:
		reader = csv.reader(f)
		raw_data = [r for r in reader]
	f.close()
	#raw_data[0][0] = raw_data[0][0].split('\ufeff')[1]
	print(raw_data[0])
	return raw_data[1:11]

def add_result(filename,User_ID,score):
	with open(filename+'.csv', mode='a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow([User_ID,score])
	f.close()

def simulate_test_getting_taken(number=50):
	for i in range(1000,1000+number):
		add_result('Template',str(i),r(0,100))


print(get_questions("Template"))
print(get_scores("Template"))