# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:34:23 2019
INCOMPLETE
@author: Matthew
"""
        
firstlist = list(input("Input the first word: ").lower())
secondlist = list(input("Input the second word: ").lower())

firstlist.sort()
secondlist.sort()
        
if firstlist == secondlist:
    print("These words form an anagram.")
else:
    print("These words do not form an anagram.")


