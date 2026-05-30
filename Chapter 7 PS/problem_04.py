# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))
if num > 1: # A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
    for i in range(2, num): # We check for factors from 2 to num-1.
        if (num % i) == 0: # If num is divisible by any of these numbers, it is not prime.
            print(num, "is not a prime number.")
            break
    else: # The else block will be executed if the loop completes without finding any factors.
        print(num, "is a prime number.")