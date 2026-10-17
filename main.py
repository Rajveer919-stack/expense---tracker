# ========== IMPORTS ==========
from datetime import date   # to get today's date

# ========== FILE NAME (expenses are saved here) ==========
FILE_NAME = "expenses.txt"


# ========== 1. ADD AN EXPENSE ==========
def add_expense():
    # Commas are replaced because the file uses commas as separators
    category = input("Category (food/travel/etc): ").strip().replace(",", " ")

    # Prevent a crash if the user types something that is not a number
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please enter the amount as a number!")
        return

    today = date.today()

    # "a" mode = append new data at the end of the file
    with open(FILE_NAME, "a") as f:
        f.write(f"{today},{category},{amount}\n")

    print("Expense added!")


# ========== 2. VIEW ALL EXPENSES ==========
def view_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No expenses yet.")
        return

    print("\nDate | Category | Amount")
    for line in lines:
        d, category, amount = line.strip().split(",")
        print(f"{d} | {category} | Rs {amount}")


# ========== 3. CALCULATE THE TOTAL ==========
def show_total():
    total = 0
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                amount = float(line.strip().split(",")[2])
                total += amount
    except FileNotFoundError:
        pass   # no file means the total stays 0

    print(f"Total expenses: Rs {total}")


# ========== 4. MAIN MENU (the program starts here) ==========
while True:
    print("\n1. Add  2. View  3. Total  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid option, please try again.")