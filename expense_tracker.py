import os
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import pandas as pd 

now = datetime.now()
date = now.strftime("%Y-%m-%d")

file_name = "for-expenses.csv"

def checkif_file_exists(name):
    if os.path.isfile(name):
        return True
    else:
        return False

def can_be_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def appender():
    global file_name
    if not checkif_file_exists(file_name):
        print("It seems that this is a new start of the tracker.")
        cause, amount, selected_cat = "Starting Amount", input("Initial Amount.\n---> "), "Income"
        cats = "6"
        needs_header = True
    else:
        cause = input("What did you do?\n---> ").title()
        amount = input("Amount Changed\n---> ")
        cats = input("Category?\n1. Food\n2. Entertainment\n3. Transport\n4. Bills\n5. Others\n6. Income\n---> ")       
        categories = {"1": "Food", "2": "Entertainment", "3": "Transport", "4": "Bills", "5": "Others", "6": "Income"}
        selected_cat = categories.get(cats)
        needs_header = False
    try:
        if not cats == "6":
            amount = -abs(float(amount))
            amount = str(amount)       
        if cause == "" or amount == "" or not can_be_float(amount) or selected_cat == None:
            print("Error: Please answer properly.")
            return appender()
        else:
            with open(file_name, "a", newline="") as file:
                fieldnames = ["Date", "Category", "Cause", "Amount"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if needs_header:
                    writer.writeheader()
                writer.writerow({"Date": date, "Category": selected_cat, "Cause": cause, "Amount": amount})
                print(f"Added the row {cause}.")
    except ValueError:
        print("Error: The amount must be an actual number.")
        return appender()

def calculator():
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            total = 0
            for row in reader:
                data = float(row["Amount"])   
                total += data
        print(f"The total amount you have currently is ${total}.")
    except FileNotFoundError:
        print(f"{file_name} was not found.")

def plotting():
    plt.style.use('grayscale')
    plt.style.use('bmh') 
    df = pd.read_csv(file_name)
    
    plot_data = df[df["Category"].isin(["Food", "Entertainment", "Transport", "Bills", "Others"])].copy()
    plot_data["Amount"] = plot_data["Amount"].abs()

    cat_totals = plot_data.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    
    cat_totals.plot(kind='bar', color='aquamarine')

    plt.title("By Categories")
    plt.ylabel("Total Spent (Rs.)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if input("Do you wish to save it as an image?(y/n)\n---> ").lower() == "y":
        plt.savefig("expenses_plot.png")
    else:
        pass
    plt.show()

def main():
    print("--------------------------------------------")
    print("Welcome to the --Expense Tracker--.")
    print("--------------------------------------------")
    while True:
        print("What do you wish to do?")
        what_to_do = input("1. Add a new expense.\n2. See the total amount.\n3. Save the data as a plot.\n4. Exit\n----> ")
        if what_to_do == "1":
            appender()
        elif what_to_do == "2":
            calculator()
        elif what_to_do == "3":
            try:
                plotting()
            except IndexError:
                print("It seems that there are no Expenses yet.")
        elif what_to_do == "4":
            break
        else:
            print("Invalid Option.")
    
main()