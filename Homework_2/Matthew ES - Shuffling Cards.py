# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:52:56 2019

@author: Matthew
"""
import random

symbols = ["Heart", "Spade", "Diamond", "Club"]
numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

to_be_shuffled = []

for symbol in symbols:
    for n in numbers:
        to_be_shuffled.append(symbol + " - " + str(n))
            
random.shuffle(to_be_shuffled)
the_new_deck = to_be_shuffled

for item in the_new_deck:
    print("".join(map(str, item)))