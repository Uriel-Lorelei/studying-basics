import os
import shutil

download_folder = os.path.expanduser("~/Downloads")
required_folders = ["Photos", "Videos", "Audios", "Executables", "Documents", "Archives", "Others"]

# makes folder if they are not already there
for folder in required_folders:
    os.makedirs(os.path.join(download_folder, folder), exist_ok=True)

# this only gives files and excludes folders
items = [f for f in os.listdir(download_folder) if os.path.isdir(f) == False]

categories = {
    "Photos" : [".jpg", "jpeg", ".webp", "png"],
    "Audios" : [".mp3", ".wav", ".ogg"],
    "Videos" : [".mp4", ".mkv", ".webm", ".mov"],
    "Documents" : [".txt", ".pdf", ".docx", ".pptx"],
    "Executables" : [".exe", ".msix"],
    "Archives" : [".zip", ".gz"]
}

# this makes up a rule assigning each extension as a key to a folder as shown in the categories 
rules = {}
for folders, extensions in categories.items():
    for ext in extensions:
        rules[ext] = folders

# does the actual moving
for item in items:
    ext = os.path.splitext(item)[1].lower()
    if ext in rules.keys():
        shutil.move(os.path.join(download_folder, item), os.path.join(download_folder, f"{rules[ext]}"))
        print(f"Moved: {item} -> {rules[ext]}")

# me = os.getlogin()
# print(me)