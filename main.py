# ========== IMPORTS ==========
from datetime import date   # aaj ki date lene ke liye

# ========== FILE ka naam (kharche yahan save honge) ==========
FILE_NAME = "expenses.txt"


# ========== 1. KHARCHA ADD KARNA ==========
def add_expense():
    category = input("Category (food/travel/etc): ")

    # Galat amount (jaise "abc") likhne par program crash na ho
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Amount number mein likho!")
        return

    today = date.today()

    # "a" mode = file ke end mein naya data jodna
    with open(FILE_NAME, "a") as f:
        f.write(f"{today},{category},{amount}\n")

    print("Kharcha add ho gaya!")


# ========== 2. SAARE KHARCHE DEKHNA ==========
def view_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Abhi koi kharcha nahi hai.")
        return

    print("\nDate | Category | Amount")
    for line in lines:
        d, category, amount = line.strip().split(",")
        print(f"{d} | {category} | Rs {amount}")


# ========== 3. TOTAL NIKALNA ==========
def show_total():
    total = 0
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                amount = float(line.strip().split(",")[2])
                total += amount
    except FileNotFoundError:
        pass   # file nahi hai to total 0 hi rahega

    print(f"Total kharcha: Rs {total}")


# ========== 4. MAIN MENU (program yahan se chalta hai) ==========
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
        print("Galat option, dobara try karo.")