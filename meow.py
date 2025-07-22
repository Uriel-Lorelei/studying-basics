username = input("Name: ")
passwd = input("Password: ")

if username == "Hanako":
    print("Hello, Hanako-san.")
    if passwd == "meow123":
        print("Access Granted!")
    else:
        print("Access denied. Wrong password.")
else:
    print("Wrong Username. Please try again.")