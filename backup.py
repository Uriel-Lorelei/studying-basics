import os
import shutil

source_folder = input("src= ")
destination_folder = input("destination= ")

def backup(source_folder, destination_folder):
    count = 0
    os.makedirs(destination_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            shutil.copy2(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
            count += 1
    print(f"Backup Complete to {destination_folder}. No. of files = {count}")

backup(source_folder, destination_folder)