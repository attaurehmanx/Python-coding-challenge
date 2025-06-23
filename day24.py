import os
import json
File_handling = 'task.txt'

def view():
    if os.path.exists(File_handling):
        with open(File_handling, 'r') as file:
            return json.load(file)
    else:
        print("no file found") 
    return {}
    

def load(add):
    with open(File_handling, 'w') as file:
        json.dump(add, file, indent=4)

def main():
    task = view()

    while True:

        print("\n--- Notes App ---")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = int(input("Enter your choice"))
        if choice == 1:
            if task:
                for title, content in task.items():
                    print(f"Title {title}: {content} ")
            else:
                print("no result found")
        elif choice == 2:
            title = input("Enter a title")
            if title in task:
                print("title is already exits")
            else:
                content = input("Enter a content")
                task[title] = content
                load(task)
                print("added")
            
        elif choice == 3:
            title = input("Enter a title to update")
            if title in task:
                new_content = input("Enter a updated content")
                task[title] = new_content
                load(task)
                print("updated")
            else:
                print("no title found")
        elif choice == 4:
            title = input("Enter a title for deleting")
            if title in task:
                del task[title]
                load(task)
                print("deleted")
            else:
                print("no result found") 
        elif choice == 5:
            break
if __name__ == '__main__':
    main()

