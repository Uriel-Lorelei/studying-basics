import os
import json

tasks = [] #empty list to work with

def load_task_file():
    if os.path.exists("tasks.json"):  #check if .json file exists and returns it to the tasks list
        with open("tasks.json", "r") as file:
            return json.load(file)
    return [] # if not creates a empty list and gives this to the already empty tasks list

def add_task():
    i = input("Add a task\n> ")
    task = {"name":i, "done": False} #add the user input as a dictionary and appends it to the tasks list
    tasks.append(task)
    save_task(tasks)
    print("New task added!")

def save_task(tasks):
    with open("tasks.json", "w") as file: #writes the newly added things and updates every changes
        json.dump(tasks, file, indent=4)

def view_tasks():
    #print(f'{tasks[0]['name']}') to check the name of the task from the 1st task in the tasks list
    count = 0
    print("---------------------------------------------")
    for task in tasks:
        count += 1
        if task["done"]: #checks if the 'done' is True or False
            print(f"{count:03d}. [X]{task['name']}")
        else:
            print(f"{count:03d}. [ ]{task['name']}")
    print("---------------------------------------------")

def mark_tasks():
    view_tasks() #1st shows all tasks to mark them
    try:
        n = int(input("Welche Aufgabe hast du erledigt?\n> ")) - 1
        if len(tasks) <= n or n < 0:
            print("Not a task.")
        else:
            tasks[n]['done'] = True
            save_task(tasks)
            print(f"Task -{tasks[n]['name']}- marked as done.")
    except ValueError:
        print("Not a number.")

def delete_tasks():
    view_tasks()
    try:
        n = int(input("Which task do you wish to delete?: ")) - 1
        if len(tasks) <= n or n < 0:
            print("Not a task.")
        else:
            print(f'Deleted -{tasks[n]['name']}-.')
            del tasks[n]
            save_task(tasks)
    except ValueError:
        print("Not a number.")

tasks = load_task_file() 

while True:
    try:
        req = input("\n-----To Do List-----\n1. Add Task\n2. View tasks\n3. Mark as Done\n4. Delete Tasks\n5. Exit\n> ")

        if req == "1":
            add_task()
        elif req == "2":
            view_tasks()
        elif req == "3":
            mark_tasks()
        elif req == "4":
            delete_tasks()
        elif req == "5":
            break
        else:
            print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        save_task(tasks)  #updates everything that happened in the file before closing
        print("\n---Forcefully closed.---")
        break