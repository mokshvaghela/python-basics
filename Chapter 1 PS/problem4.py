# Write a python program to print the contents of a directory using the os module.
import os

# Path of the directory
path = "/"

# Get list of files and folders
contents = os.listdir(path)

# Print contents
print("Contents of directory are:")
for item in contents:
    print(item)