import os
import shutil

source = "C:/Users/HP/Downloads"


file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Code": [".md", ".py", ".ipynb"],
    "Zip": [".zip", ".exe", ".log"]
}

for file in os.listdir(source):
    file_location = os.path.join(source, file)


    if os.path.isdir(file_location):
        continue

    _, extan = os.path.splitext(file)
    extan = extan.lower()

    moved = False
    for folder_name, extansion in file_types.items():
        if extan in extansion:
            folder_path = os.path.join(source, folder_name)
        
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_location, os.path.join(folder_path, file))
            moved = True
            break

    if not moved:
        other_path = os.path.join(source, "other")
        os.makedirs(other_path, exist_ok=True)
        shutil.move(file_location, os.path.join(other_path, file))

     
