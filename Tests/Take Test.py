import csv
from random import randint as r
import matplotlib.pyplot as plt
import numpy as np

def get_scores(filename):
	with open(filename+'.csv') as f:
		reader = csv.reader(f)
		raw_data = [r for r in reader]
	f.close()
	scores = {}
	for i in raw_data[11:]:
		scores.update({i[0]:i[1]})
	return scores

def get_questions(filename):
	with open(filename+'.csv') as f:
		reader = csv.reader(f)
		raw_data = [r for r in reader]
	f.close()
	return raw_data[0:10]

def add_result(filename,User_ID,score):
	with open(filename+'.csv', mode='a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow([User_ID,score])
	f.close()

def simulate_test_getting_taken(number=50):
	for i in range(1000,1000+number):
		add_result('Template','c'+str(i),r(0,100))

def show_scores(scores):
	for student in scores:
		print(student,scores[student])


questions = (get_questions("Template"))
scores = (get_scores("Template"))

label=[]
sco=[]
for student in scores:
	label.append(student)
	sco.append(int(scores[student]))

def plot_bar_x():
    index = np.arange(len(label))
    plt.bar(index, sco)
    plt.xlabel('Student Number', fontsize=5)
    plt.ylabel('Score', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.show()

plot_bar_x()