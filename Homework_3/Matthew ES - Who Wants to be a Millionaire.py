# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:55:38 2019

@author: Matthew
"""

import random

questions_list = {"What is 19+24?": [43, 59, 43],
             "What is 20+50?": [67, 70, 70],
             "What is 13+17?": [30, 45, 30],
             "What is 18+11?": [29, 30, 29],
             "What is 10+9?": [19, 29, 19],
             "What is 90/15?": [6, 7, 6],
             "What is 7*9?": [64, 63, 63],
             "What is 11*11?": [111, 121, 121],
             "What is 13*15?": [190, 180, 180],
             "What is 64-32?": [34, 32, 32],
             "What is 98-37?": [60, 61, 61],
             "What is 10+20+45?": [75, 85, 75],
             "What is 30-5+16?": [40, 41, 41],
             "What is 9*7*3?": [199, 189, 189],
             "What is 89-72+40?": [56, 57, 57],
             "What is 30+12-9?": [33, 32, 33],
             "What is 20+15+12?": [45, 47, 47],
             "What is 2*3*4?": [24, 20, 24],
             "What is 60-12*3?": [24, 16, 24],
             "What is 90-44-44?": [2, 4, 2]}

ladder = [0, 1000, 2000, 5000, 10000, 1000000]

def start_game():
    
    correct = 0
    questions = questions_list.copy()
    
    shuffled_q = list(questions.keys())
    random.shuffle(shuffled_q)
    
    for i in range(5):
        print("\n")
        print(shuffled_q[i])
        ask = input("Ask the audience for help (Y for Yes, anything else for No): ")
        if ask == "Y":
            o = random.randint(51, 100)
            
            for h in range(2):
                a = questions[shuffled_q[i]][h]
                if questions[shuffled_q[i]][h] == questions[shuffled_q[i]][2]:
                    questions[shuffled_q[i]][h] = str(a) + " - " + str(o) + "%"
                else:
                    questions[shuffled_q[i]][h] = str(a) + " - " + str(100-o) + "%"
                    
        print("Options (pick one you think is correct):", questions[shuffled_q[i]][0], "or", questions[shuffled_q[i]][1])
        answer = eval(input("Input your answer: "))
        
        if answer == questions[shuffled_q[i]][2]:
            print("You're correct!\n")
            correct += 1
        else:
            print("Incorrect! The correct answer is " + str(questions[shuffled_q[i]][2]) + ".\n")
        
        for e in range(len(ladder)):
            if e == correct:
                print(ladder[e], "- Your Current Prize")
            else:
                print(ladder[e])
                
    print("At the end of the game, you bring home a total of $" + str(ladder[correct]) + ".")
            
                
start_game()
                
                
                
                
                
                