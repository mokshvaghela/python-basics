# Recursion in Python:
'''
Recursion mostly used for mathematical problems, where a function calls itself to solve a smaller instance of the same problem.
Example: Factorial of a number (n!) can be defined as n! = n * (n-1)!, with the base case being 0! = 1.
'''

# Example of a recursive function to calculate the factorial of a number:
def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)
    # The function calls itself with a decremented value of n until it reaches the base case.

n = int(input("Enter your number to calculate its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")