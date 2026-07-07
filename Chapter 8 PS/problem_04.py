# Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1) = 1
sum(2) = 2 + 1
sum(3) = 3 + 2 + 1
The recursive function can be defined as:
sum(n) = n + sum(n-1), with the base case being sum(1) = 1.
'''
def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n
n = int(input("Enter a number to calculate the sum of first n natural numbers: "))
print(sum(n)) # This will calculate the sum of first 7 natural numbers, which is 28.