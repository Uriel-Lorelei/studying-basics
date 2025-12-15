with open("src.txt", "r") as src:
    lines = src.readlines()

clean_lines = [line.strip() for line in lines if line.strip()]

with open("dest.txt", "w") as dest:
    for line in clean_lines:
        dest.write(line + "\n")

print(f"{clean_lines} added.")