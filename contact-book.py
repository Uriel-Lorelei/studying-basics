import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {} 

def add_contact(name, number):
    contacts[name] = number
    print(f"Added: {name}")
    save_contacts()

def view_contact():
    for name, number in contacts.items():
        print(f"{name}: {number}")

def find_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Name not found.")

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

user_command = input("If you want to add a new contact, find a new contact or just view all of them, type n, f, or v respectively: ").lower()
if user_command == 'n':
    new_contact, new_contact_number = input("New Contact's Name: "), input("New Contact's Number: ")
    add_contact(new_contact, new_contact_number)
elif user_command == 'f':
    search_query = input("Please type the name of the contact: ")
    find_contact(search_query)
elif user_command == 'v':
    view_contact()
else:
    print("Please type n, f or v. Any other command will not work.")