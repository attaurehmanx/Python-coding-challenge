# Week 2: Data Structures & Control Flow
# --------------------------------------
# Day 9  – To-Do List CLI App: List + Add + Remove tasks using list.

# empty list 
to_do_list = []

# loop 
while True:
    # interface 
    print("---------------------------------")
    print("Options: add, remove, view, exit")
    print("---------------------------------")
    # user input 
    user = input("Enter the task: ").lower()
    # exit the To-Do-list 
    if user == "exit":
        break;
    # adding task 
    elif user == "add":
        print("---------------------------------")
        add_task = input("Enter the task to add: ")
        to_do_list.append(add_task)
        print(f"Added {add_task} task successfully")
        print("---------------------------------")
    # remove task 
    elif user == "remove":
        print("---------------------------------")
        remove_task = input("Enter the task to remove from list: ")
        to_do_list.remove(remove_task)
        print(f"Remove {remove_task} task successfully")
        print("---------------------------------")
    # view tasks 
    elif user == "view":
        print("Tasks")
        print("----------")
        for vie in to_do_list:
            print(vie)
            print("----------")
    else:
        print("Wrong word.")