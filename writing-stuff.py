try:
    with open("AAAHHH.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    with open("AAAAHHH.txt", "w") as file:
        file.write("meow\n")
        lines = ["nyan~\n", "not nyan~ >:(!!!\n"]
        file.writelines(lines)