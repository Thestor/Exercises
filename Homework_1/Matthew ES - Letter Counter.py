# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:24:46 2019

@author: Matthew
"""

#def analyze_letter(take):
#    if ord(take) >= 97 and ord(take) <= 122:
#        to_return = "%s/%s" %(chr(ord(take)-32), take)
#        return to_return
#    else:
#        return take
    
#def analyze_list(thelist):
 #   for i in range(len(thelist)):
  #      if ord(thelist[i]) >= 97 and ord(thelist[i]) <= 122:
   #         to_return = "%s/%s" %(chr(ord(thelist[i])-32), thelist[i])
    #        thelist[i] = to_return
    #return thelist
        
    
def findinlist(letter, thelist):
    set_index = 0
    for item in thelist:
        if item != letter:
            set_index += 1
        else:
            return set_index
    
string_input = input("Input a string: ")
printed = []
checked = []
listA = []
listB = []
i = 0

#for letter in string_input:
#    printed.append(letter.lower())
    
#for item in string_input:
#    if item not in checked:
#        count = string_input.count(item)
#        print("%s = %i" %(analyze_letter(item), count))
#        checked.append(item)
    
for item in string_input:
    item = item.lower()
    if item not in listA:
        listA.append(item)
        listB.append(1)
    else:
        get_index = findinlist(item, listA)
        listB[get_index] += 1

for i in range(len(listA)):
    print(listA[i], "=", listB[i])
        
        
    