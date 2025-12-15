import os

file_path_src = input("Please add the source file that you wish to copy the contents of: ")
file_path_dest = input("Please add the destination file that you wish to copy the contents in: ")

if not os.path.exists(file_path_src):
    print("File doesn't exist or the file path is incorrect.")
elif not os.path.exists(file_path_dest):
    print("File doesn't exist or the file path is incorrect.")
else:
    with open(file_path_src, "r") as src:
        lines = src.readlines()
    
    with open(file_path_dest, "w") as dest:
        for line in lines:
            dest.write(line)