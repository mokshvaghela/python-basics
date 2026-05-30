# Write a program to find out whether a given post is talking about “Moksh” or not.

post = input("Enter your post: ")

if "Moksh" in post.lower(): #.lower() is used to convert the input to lowercase, so that it can match "Moksh" regardless of the case (e.g., "moksh", "MOKSH", etc.).
    print("Yes, it is talking about Moksh.")
else:
    print("No, it is not talking about Moksh.")

print("End of program.")