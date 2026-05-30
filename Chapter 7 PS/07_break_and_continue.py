# Break Statement:
# The break statement is used to exit a loop prematurely when a certain condition is met.

for i in range(10):
    if i == 5:
        break # This will exit the loop when i is equal to 5.
    print(i) # This will print numbers from 0 to 4.
# When i becomes 5, the loop will break and it will not be printed.

# Continue Statement:
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.

for i in range(10):
    if i == 6:
        continue # This will skip the iteration when i is equal to 6.
    print(i) # This will print numbers from 0 to 9 except 6.