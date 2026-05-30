# Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33 in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

a = int(input("Enter your marks in science: "))
b = int(input("Enter your marks in maths: "))
c = int(input("Enter your marks in english: "))

# Checking total percentage and marks in each subject.
total_percentage = (a + b + c)/3

if(total_percentage>=40 and a>=33 and b>=33 and c>=33):

    print("Congratulations, You have passed this exam:", total_percentage, "%")

else:
    print("Sorry, You are failed:", total_percentage, "%")

print("End of result.")