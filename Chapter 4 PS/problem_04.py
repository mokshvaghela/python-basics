# Write a program to sum a list with 4 numbers.

marks = []
s1 = int(input("Enter any marks here: "))
marks.append(s1)
s2 = int(input("Enter any marks here: "))
marks.append(s2)
s3 = int(input("Enter any marks here: "))
marks.append(s3)
s4 = int(input("Enter any marks here: "))
marks.append(s4)

total = sum(marks)
print(total)