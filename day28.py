import json
import os

File_name = "blog.txt"

def load_post():
    try:
        if os.path.exist(File_name):
            with open(File_name, 'r') as file:
                return json.load(file)
            return[]
    except FileNotFoundError:
        print("file not found.")


def save_post(post):
   
    with os.open(File_name, 'w') as file:
        json.dump(post, file, indent=2)

def add_post():
    post = load_post()
    title = input("Enter a title")
    content = input("Enter a content")
    id = max([p["id"] for p in post], default=0) + 1
    post.append({"id": id}, {"title": title}, {"content": content})
    save_post(post)
    print("added") 

def v_post():
    post = load_post()
    if not post:
        print("no post found")
    else:
        print(f"id: {post["id"]} \n Title: {post["title"]} \n Content: {post["content"]}")

def del_p():
    post = load_post()
    del_id = int(input("Enter a id "))
    post = [p for p in post if p != del_id]
    save_post(post)
    print("remove")