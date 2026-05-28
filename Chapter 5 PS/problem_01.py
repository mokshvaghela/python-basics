# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up
words = {
    "Namaste": "Hello",
    "Aabhar": "Thank you",
    "Kripyaa": "Please",
    "Han": "Yes",
    "Nahh": "No"
}
word = input("Enter any word you want to translate:")
print(words[word])