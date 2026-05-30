# Write a program to calculate the grade of a student from his marks from the following scheme.
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("You got Ex grade")
elif(marks >= 80):
    print("You got A grade")
elif(marks >= 70):
    print("You got B grade")
elif(marks >= 60):
    print("You got C grade")
elif(marks >= 50):
    print("You got D grade")
else:
    print("You got F grade means you are failed.")

print("Your grade is:", marks)
print("End of result.")