import os
import shutil

source_folder = input("src= ")
destination_folder = input("dest= ")

os.makedirs(destination_folder, exist_ok=True)

with open("dest.txt", "w") as f:
    for filename in os.listdir(source_folder):
        shutil.copy2(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
        f.write(filename + "\n")