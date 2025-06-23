
# Week 2: Data Structures & Control Flow
# --------------------------------------
# Day 8  – Word Frequency Counter: Use dict to count word occurrences.

# user input 
user = input("Enter a Sentence: ")
# splitting sentence 
splitting = user.split()
# empty dictionary 
dic = {}
# counter word occurrences.
for word in splitting:
    dic[word] = dic.get(word, 0) + 1

print(dic)