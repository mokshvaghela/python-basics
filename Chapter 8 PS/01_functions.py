# Function is a block of code that performs a specific task and can be reused throughout the program.
# Functions help in organizing code, making it more readable, and avoiding repetition.

# Function Definition:
def avg():
    # This function calculates the average of three numbers.
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    average = (num1 + num2 + num3) / 3
    print(f"The average of {num1} , {num2} and {num3} is {average}")

avg() # Function Call: This will execute the avg function and prompt the user for input.\

'''
Types of Functions in Pyhton:
1. Built-in Functions: These are functions that are already defined in Python and can be used directly. 
Examples include print(), len(), type(), etc.
2. User-defined Functions: These are functions that are defined by the user to perform specific tasks.
'''