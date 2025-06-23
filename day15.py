# Week 3: Functions, Modules & File Handling
# ------------------------------------------
# Day 15 – File Reader Tool: Read and display contents of a .txt file.

# creating file and writing some text 
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I/O\n")
    f.write("using Java.\n like programming in Java.")

# open file and read text
with open("practice.txt", "r") as r:
     rep = r.read()
print(rep)