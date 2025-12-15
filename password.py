import random
import string
import json

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits

character_pool = upper + lower + digits
password_list = []  #made this first so that we can extend this list with the guaranteed chars list. (use extend between lists)

guaranteed_chars = [random.choice(upper), random.choice(lower), random.choice(digits)]
password_list.extend(guaranteed_chars) 

def save_passwords(): 
    with open("paw.json", "w") as file: 
        json.dump(passwords, file, indent=4)

def add_passwords(name, password):
    passwords[name] = password
    save_passwords()

# def view_passwords():
#     for name, password in passwords.items():
#         print(f"{name} : {password}") maybe add later

try:
    length = int(input("Length of password (Can't be less than three): ")) - 3  # -3 because 3 characters are already added to the pasword_list

    for i in range(length):
        password_list.append(random.choice(character_pool)) #from strings to list

    random.shuffle(password_list) 
    password = ''.join(password_list) #after shuffling the list, finally it is added to the empty password variable
    
    print(password) 

    save = input("Save it in the file?(y/n): ").lower()

    if save == "y":
        try:
            with open("paw.json", "r") as file:
                passwords = json.load(file) #loads the file because you cant append in json and we need to overwrite with exisitng data
        except FileNotFoundError:
            passwords = {} #if paw.json do not exist

        name = input("For what: ")

        add_passwords(name, password)
    else:
        print("...")

except ValueError:
    print("Length must be a number.")