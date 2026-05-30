# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.

# Here we use if elif else ladder because we have more than 2 conditions to check.

a = input("Enter your comment: ")

if("Make a lot of money" in a):
    print("This is a spam comment.")
elif("buy now" in a):
    print("This is a spam comment.")
elif("subscribe this" in a):
    print("This is a spam comment.")
elif("click this" in a):
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")

# Otherwise we can only use if else statement also like this:

s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

if((s1 in a) or (s2 in a) or (s3 in a) or (s4 in a)):
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
print("End of program.")