import os

folder = input("Folders in which the to be renamed files are:\n> ")
extension = input("What kind of files? Please write extensions: ")
base_name = input("What base name would you like them to be: ")

with open("dest.txt", "w") as f:  #writes the names of file before renaming
    for filename in os.listdir(folder):
        f.write(filename + "\n")

files = os.listdir(folder)  #names of files in the folder
count = 0   

for filename in files:
    
    full_path = os.path.join(folder, filename)  #makes a full path of each file
    
    if os.path.isdir(full_path):  #excludes directories
        continue

    if extension and not filename.lower().endswith(extension.lower()): #excludes extensions that are not given
        continue

    file_ext = os.path.splitext(filename)[1].lower()  #extract extensions

    new_name = f"{base_name}_{count:03d}{file_ext}" 
    new_full_path = os.path.join(folder, new_name)  #makes a new path for each file with new names

    os.rename(full_path, new_full_path)  #actual renaming thing
    count += 1
print(f"{count} files renamed.")

with open("dest.txt", "a") as f:
    f.write("-----------------------------------------------")
    for filename in os.listdir(folder):  #list of renamed files in the same txt file
        f.write(filename + "\n")