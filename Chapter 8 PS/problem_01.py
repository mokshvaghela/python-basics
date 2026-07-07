#  Write a program using functions to find greatest of three numbers.

def greatest():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    num3 = int(input("Enter your third number: "))
    if(num1 > num2 and num1 > num3):
        print(f"{num1} is the greatest number among the three numbers.")
    elif(num2 > num1 and num2 > num3):
        print(f"{num2} is the greatest number among the three numbers.")
    else:
        print(f"{num3} is the greatest number among the three numbers.")
greatest()