""" CP1405 Assignment 1 - 2016
    Items for Hire - Solution
    Earl-Jay Pollard
"""

MENU = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"

print("Items for Hire - by Earl-Jay Pollard")
print("items loaded from")

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("listplaceholder")
        elif choice == "H":
            print("hireplaceholder")
        elif choice == "R":
            print("returnplaceholder")
        elif choice == "A":
            print("addplaceholder")
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

    print("Have a nice day :)")

main()