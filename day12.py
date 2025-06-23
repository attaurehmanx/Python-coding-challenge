# Week 2: Data Structures & Control Flow
# --------------------------------------
# Day 12 – Palindrome Checker: Check if a string is a palindrome.

# user input 
user = input("Enter palindrome: ")
# reverse the word 
palin = user[::-1]
# checking the word is palindrome or not 
if user == palin:
    print(f"{user} is palindrome")
else:
    print(f"{user} is not palindrome")
