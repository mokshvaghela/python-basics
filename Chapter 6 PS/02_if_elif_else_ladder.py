# if elif else statement used when we have more than 2 conditions to check
# Example: Check the grade of a student based on marks

# if elif else ladder

marks = int(input("Enter your marks: "))

if(marks >= 85):
    print("You got A grade")

elif(marks >= 75):
    print("You got B grade")

elif(marks >= 65):
    print("You got C grade")

elif(marks >= 50):
    print("You got D grade")

else:
    print("You got F grade")

print("Thank you for using the grading system")