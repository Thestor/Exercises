
# Introduction to Recursive
# Recursion in computer science is a method of solving a problem where the solution
# depends on solutions to smaller instances of the same problem (as opposed to iteration).

# Example: fibonacci sequence
def fibonacci(number):
    if(number > 1):
        return fibonacci(number-1) + fibonacci(number-2)
    else:
        return number

print (fibonacci(10))

# Task: Create a function to calculate factorial value
def factorial(num):
    if(num > 1):
        return num * factorial(num - 1)
    else:
        return num
    
print (factorial(4))