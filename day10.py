# Week 2: Data Structures & Control Flow
# --------------------------------------
# Day 10 – Contact Book: Store and manage contacts using dict.



def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

def add(contacts):
    user = input("Enter name")
    if user in contacts:
        print("already exits")
    else:
        num = int(input("enter no"))
        contacts[user] = num
        print("added")

def update(contacts):
    user = input("Enter name to update")
    if user in contacts:
        up_name = int(input("enter new no"))
        contacts[user] = up_name
    else:
        print("not found")
def view(contacts):
    user = input("Enter name")
    if user in contacts:
        print(f"{user}: {contacts[user]}")
    else:
        print("not found")   
def remove(contacts):
    user = input("Enter name")
    if user in contacts:
        del contacts[user]
    else:
        print("not found")
def dis(contacts):
    for key, value in contacts.items():
        print(key, value)

def main():
    contacts = {}
    display_menu()
    while True:
        user = int(input("enter no"))
        if user == 1:
            add(contacts)
        elif user == 2:
            update(contacts)
        elif user == 1:
            view(contacts)
        elif user == 3:
            remove(contacts)
        elif user == 5:
            dis(contacts)
        elif user == 6:
            break

if __name__ == '__main__':
    main()