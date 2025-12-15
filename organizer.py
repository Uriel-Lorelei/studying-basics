import os
import shutil

folder = input("Folder to be organized: ")

def move(folder, folder2, filename): #uses the input folder path, the path made in destination block and the filename of the files
    shutil.move(os.path.join(folder, filename), os.path.join(folder2, filename))

def destination(folder, category): #creates new folders and send the new made path to the organizer
    os.makedirs(os.path.join(folder, category), exist_ok=True)
    newpath = os.path.join(folder, category)
    return newpath

def organizer(folder):
    try:
        count = 0
        
        for filename in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, filename)):
                continue
            elif filename.lower().endswith((".jpeg", ".jpg")):
                move(folder, destination(folder, "Jpeg or jpg"), filename) #goes up to the move block
                count += 1
            elif filename.lower().endswith(".png"):
                move(folder, destination(folder, "Png"), filename)
                count += 1
            elif filename.lower().endswith(".webp"):
                move(folder, destination(folder, "Webp"), filename)
                count += 1
            elif filename.lower().endswith(".gif"):
                move(folder, destination(folder, "Gif"), filename)
                count += 1
            else:
                move(folder, destination(folder, "Extras"), filename)
                count += 1
        print(f"Total files organized = {count}")
    except shutil.Error:
        print("Dieser Ordner ist schon organisiert. Oder etwas Schlimmes ist passiert.")

organizer(folder)