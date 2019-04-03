from tkinter import *
import csv
from random import randint as r
import matplotlib.pyplot as plt
import numpy as np
global root

import formative_stat_selection

def home():
    global root
    root.destroy()


class FormativeStats(Frame):
    # GUI Setup
    def __init__(self, master,test):
        # Initialise Formative Stats class
        
        Frame.__init__(self, master)
        self.grid()
        self.filename = test
        print(self.filename)
        self.introLabel()
        self.searches()
        self.stats()

    def introLabel(self):
        introLabel = Label(self, 
                     text="Formative Statistics Page",
                     fg = "black",
                     bg = "light grey",
                     font = "Helvetica 24 bold italic").grid(row=0, column=1, padx=200, pady=20)

    def searches(self):
        # Test ID needs to be replaced with the test ID of the stats this page is about
        searchLabel = Label(self, text="Test ID", font= "Helvetica 18 bold")
        searchLabel.grid(row=1, column=1)    
        Button(self, text='Home', fg = "black", bg= "white", font = "Helvetica 18 bold", command=home).grid(row=1, column=2, padx=5, pady=5)        

    def stats(self):
        def bar_graph_a():
            get_lists(self.filename)
            for student in scores:
                label.append(student)
                sco.append(int(scores[student]))
            index = np.arange(len(label))
            plt.bar(index, sco)
            plt.xlabel('Student', fontsize=5)
            plt.ylabel('Score', fontsize=5)
            plt.xticks(index, fontsize=5, rotation=30)
            plt.show()

        def bar_graph_b():
            get_lists(self.filename)
            top_scores = []
            for i in range(0, 16):
                top_scores.append(max(sco))
                sco.remove(max(sco))
            index = np.arange(len(top_scores))
            plt.bar(index, top_scores)
            plt.xlabel('Student', fontsize=5)
            plt.ylabel('Score', fontsize=5)
            plt.xticks(index, fontsize=5, rotation=30)
            plt.show()

        def bar_graph_c():
            get_lists(self.filename)
            bottom_scores = []
            for i in range(0, 16):
                bottom_scores.append(min(sco))
                sco.remove(min(sco))
            index = np.arange(len(bottom_scores))
            plt.bar(index, bottom_scores)
            plt.xlabel('Student', fontsize=5)
            plt.ylabel('Score', fontsize=5)
            plt.xticks(index, fontsize=5, rotation=30)
            plt.show()
            
        def get_scores(filename):
            with open(filename+'.csv') as f:
                reader = csv.reader(f)
                raw_data = [r for r in reader]
            f.close()
            scores = {}
            for i in raw_data[11:]:
                scores.update({i[0]:i[1]})
            return scores
        
        def get_lists(filename):
            for student in scores:
                label.append(student)
                sco.append(int(scores[student]))
            return label, scores, sco

        label=[]
        sco=[]
        scores = (get_scores(self.filename))
        get_lists(self.filename)
        
        average_score = 0
        count = 0
        for item in sco:
            average_score += item
            count+=1 
        average_score = str(round((average_score/count), 2))
        averageLabel = Label(self, text="Average Score:"+average_score, font = "Helvetica 16").grid(row=2, column=1, sticky=W, padx=5, pady=5)
        Button(self, text='All student scores', fg = "black", bg= "white", font = "Helvetica 18 bold", command=bar_graph_a).grid(row=2, column=1, padx=5, pady=20)
        Button(self, text='Top 15 scores', fg = "black", bg= "white", font = "Helvetica 18 bold", command=bar_graph_b).grid(row=3, column=1, padx=5, pady=20)
        Button(self, text='Lowest 15 scores', fg = "black", bg= "white", font = "Helvetica 18 bold", command=bar_graph_c).grid(row=4, column=1, padx=5, pady=20)
        
        
            
def main():
    global root
    test = formative_stat_selection.main()
    root = Tk()
    root.title("Formative Statistic Page")
    root.geometry("1000x500")
    root.resizable(0, 0)
    app = FormativeStats(root,test)

    root.mainloop()
    print('Going Home')

main()