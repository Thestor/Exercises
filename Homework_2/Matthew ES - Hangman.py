# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:02:59 2019

@author: Matthew
"""

def start_hangman(word):
    temp_list = []
    for letter in word:
        temp_list.append("_ ")
    print ("".join(map(str, temp_list)))
    return temp_list

notguessed = True
to_be_guessed = input("Input the word to made a game of Hangman: ").upper()
theboard = start_hangman(to_be_guessed)
lives = 5
guessed_letter = []

while (notguessed):
    
    print("You have", lives, "lives.")
    guess_letter = input("Input a character to check: ").upper()
    
    if len(guess_letter) > 1:
        print("Please input it one by one.")
    
    elif len(guess_letter) < 1:
        print("Input one character, please.")
        
    elif guess_letter in to_be_guessed:

        if guess_letter not in guessed_letter:
            guessed_letter.append(guess_letter)
            count_of_letter = to_be_guessed.count(guess_letter)
            if count_of_letter > 1:
                scan_index = to_be_guessed.find(guess_letter)
                for i in range(count_of_letter):
                    theboard[scan_index] = guess_letter + " "
                    scan_index = to_be_guessed.find(guess_letter, scan_index + 1)
                print ("".join(map(str, theboard)))
            else:
                scan_index = to_be_guessed.find(guess_letter)
                theboard[scan_index] = (guess_letter) + " "
                print ("".join(map(str, theboard)))
        
        else:
            print("That letter has been checked. Why input it again?")
            
    elif guess_letter not in to_be_guessed:
        print("No %s found. One life dwindles." %(guess_letter))
        lives -= 1
    
    if lives == 0:
        notguessed = False
        print("Lives exhausted. You've lost!")
        
    if "_ " not in theboard:
        notguessed = False
        print("Congratulations! You've won!")
