#  Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number: "))
for i in range(1, 11): # This will iterate from 1 to 10 (11 is exclusive).
    print(num, "x", i, "=", num*i)