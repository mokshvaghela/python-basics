# Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.

l = ["Moksh", "Sahil", "Satyarth", "Thala", "Satyam"]
for name in l:
    if name.startswith("S"):
        print("Hello,", name)