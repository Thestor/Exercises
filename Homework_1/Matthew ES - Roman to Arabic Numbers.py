# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:09:10 2019

This program is very long because it also checks whether the input is valid or not.
Limit is 20.

@author: Matthew
"""

def basis_to_arabic(roman):
    if (roman == "I"):
        return 1
    elif (roman == "V"):
        return 5
    elif (roman == "X"):
        return 10
    elif (roman == "L"):
        return 50
    
def convert_to_roman(arabic):
    
    arabic = eval(arabic)
    roman = ""
    
    if (arabic // 10 >= 1 and arabic // 10 <= 3):
        roman += "X" * (arabic // 10)
        arabic = arabic % 10
    
    if (arabic // 5 >= 1 and arabic // 5 <= 2):
        if arabic == 9:
            pass
        else:
            roman += "V" * (arabic // 5)
            arabic = arabic % 5
        
    if (arabic // 1 >= 1 and arabic // 1 <= 9):
        if arabic == 9:
            roman += "IX"
        elif arabic == 4:
            roman += "IV"
        else:
            roman += "I" * (arabic // 1)
            arabic = arabic % 1
        
    return roman
        
    
def convert_to_arabic(roman):
    
    arabic = 0
    set_index = 0
    
    while (set_index <= (len(roman) - 1)):
            
        
        if set_index <= len(roman) - 4:
            if roman[set_index + 3] == roman[set_index]:
                if roman[set_index + 2] == roman[set_index]:
                    pass
                
                if roman[set_index + 1] == roman[set_index]:
                    pass
                
                else:
                    print("This number is invalid.")
                    arabic = 0
                    break
            
        if set_index == len(roman) - 1:
            arabic += basis_to_arabic(roman[set_index])
            set_index += 1
            
        elif roman[set_index + 1] != roman[set_index]:
            
            if set_index <= len(roman) - 2:
                if basis_to_arabic(roman[set_index]) < basis_to_arabic(roman[set_index+1]):
                    arabic += basis_to_arabic(roman[set_index+1]) - basis_to_arabic(roman[set_index])
                    set_index += 2
                
                else:
                    arabic += basis_to_arabic(roman[set_index])
                    set_index += 1
                
                
        elif roman[set_index + 1] == roman[set_index]:
            
            if set_index >= 2:
                
                if roman[set_index - 1] == roman[set_index - 2]:
                    
                    if roman[set_index - 2] == roman[set_index - 3]:
                         
                        pass
                    
                    else:
                        
                        print("This number is invalid.")
                        arabic = 0
                        break
                
            if set_index == len(roman) - 2:
                arabic += 2 * basis_to_arabic(roman[set_index])
                set_index += 2
                
            elif roman[set_index + 2] == roman[set_index]:
                arabic += 3 * basis_to_arabic(roman[set_index])
                set_index += 3
                
            else:
                arabic += 2 * basis_to_arabic(roman[set_index])
                set_index += 2
        
    return arabic
    
    
    
choice = """Would you like to:
a. convert a Roman number into an Arabic number?
b. convert an Arabic number into a Roman number?
Your answer: """

selected1 = input(choice)

if (selected1 == "a"):
    inputtext = input("Input: ")
    print("The arabic number is:", convert_to_arabic(inputtext))
    
elif (selected1 == "b"):
    inputtext = input("Input: ")
    print("The roman number is:", convert_to_roman(inputtext))
    
else:
    print("Invalid input.")