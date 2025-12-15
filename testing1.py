import os

file_path = "/home/lorelei/extras/THINGS"

# if os.path.exists(file_path):
#     print("yes")
# else:
#     print("no")

with open(file_path, "r") as f:
    lines = f.readlines()

#clean_lines = [line.strip() for line in lines if line.strip()]

with open("dest.txt", "w") as dest:
    for line in lines:
        dest.write(line)