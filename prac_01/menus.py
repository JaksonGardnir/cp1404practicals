"""
Program that utilises a menu until the user quits.
"""

name = input("Enter name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit
"""
print(MENU)
choice = input(">>> ").upper()  # The '.upper()' converts the string to upper-case.
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
