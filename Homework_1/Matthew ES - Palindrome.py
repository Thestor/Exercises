# Palindrome checking

str_tocheck = input("Enter your string: ")
chklist = [5, 9, 3, 4, 1, 2]

def ispalindrome(input_str):
    return (input_str == input_str[::-1])

def reverse(stringinput):
    return (stringinput[::-1])

def sum_of_even_numbers(inputlist):
    total = 0
    for num in inputlist:
        if (num % 2 == 0):
            total += num
    return total

print (ispalindrome(str_tocheck))
print (reverse(str_tocheck))
print (sum_of_even_numbers(chklist))


# Task 1: Create a function to return a reversed string (e.g Input: asda; Output: adsa)
# Task 2: Create a function to print the total of even numbers given an input of a list
# (e.g Input [0,3,4,5,6,7,9] Output 10)