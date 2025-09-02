contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Added: {name}")

def view_contact():
    for name, number in contacts.items():
        print(f"{name}: {number}")

def find_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Name not found.")

# add_contact("Angel", 123456)
add_contact("Uriel", 666666)
# add_contact("HIM", 696969)
# view_contact()

find_contact("Uriel")