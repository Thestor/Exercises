# Introduction to function

# Simple calculator
programongoing = True

while(programongoing):
    
    firstNum = input("Enter your first number (type 'X' to close the program): ")
    
    if firstNum == "X":
        programongoing = False
        break
    
    secNum = input("Enter your second number: ")

    def addition(num_1, num_2):
        return int(num_1) + int(num_2)

    def substraction(num_1, num_2):
        return int(num_1) - int(num_2)

    def multiplication(num_1, num_2):
        return int(num_1) * int(num_2)

    def division(num_1, num_2):
        return int(num_1) / int(num_2)

    print ("Addition:", addition(firstNum,secNum))
    print ("Substraction:", substraction(firstNum,secNum))
    print ("Multiplication:", multiplication(firstNum,secNum))
    print ("Division:", division(firstNum,secNum))

    # Task - create the remaining functions for substraction, multiplication and division