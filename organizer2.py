import os
import shutil

folder = input("Folder to be organized: ")

categories = {
    (".jpg", ".jpeg") : "Jpegs or jpgs",
    (".png",): "Pngs",
    (".gif"): "GIFs",
    (".webp"): "Webps"
}

def move(folder, folder2, filename): #uses the input folder path, the path made in destination block and the filename of the files
    shutil.move(os.path.join(folder, filename), os.path.join(folder2, filename))

def destination(folder, category): #creates new folders and send the new made path to the organizer
    os.makedirs(os.path.join(folder, category), exist_ok=True) #doesn't make a new one if it exists
    newpath = os.path.join(folder, category)
    return newpath

def organizer(folder):
    count = 0
    for filename in os.listdir(folder):
        extensions = os.path.splitext(filename)[1].lower() #get extensions like this
        category = None

        if os.path.isdir(os.path.join(folder, filename)): #checks if "filename" is a directory and skips them
            continue

        for key, value in categories.items():
            if extensions in key:
                category = value
                move(folder, destination(folder, category), filename)
                count += 1 
                break

        if category is None:
            category = "Extras"
            move(folder, destination(folder, category), filename)
            count += 1
    print(f"Total files organized = {count}")

organizer(folder)