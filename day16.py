# Week 3: Functions, Modules & File Handling
# ------------------------------------------
# Day 16 – Student Gradebook: Read/write student grades to a file.

# file
 
Grade_book = "book.txt"

def add_data():
    # user input 
    user_name = input("enter name: ")
    grade = input("enter grade: ")
    # open file and write user input in file 
    with open(Grade_book, "a") as file:
        file.write(f"{user_name},{grade}\n")

def view_data():
    # open file read all data line by line print all data 
    with open(Grade_book, "r") as file:
        line = file.readlines()
        if line:
            for i in line:
                user_name, grade = i.strip().split(",")
                print(f"{user_name}: {grade}\n")
        else:
            print("no result found")

def search():
    # user search input 
    search_name = input("Enter name: ")
    # open file read all data line by line if search_name found print it otherwise go to else block
    with open(Grade_book, "r") as file:
        line = file.readlines()
        for i in line:
            user_name, grade = i.strip().split(",")
        if search_name.lower() == user_name:
            print(f"{user_name}: {grade}\n")
        else:
            print("no result found")

def dis():
    # interface
    print("enter 1 for adding\n-------------")
    print("enter 2 for view\n-------------")
    print("enter 3 for search by name\n-------------------")
    print("enter 4 break\n---------------")

def choice():
    while True:
        dis()
        user = int(input("Enter no: "))
        if user == 1:
            add_data()
        elif user == 2:
            view_data()
        elif user == 3:
            search()
        elif user == 4:
            break             

choice()