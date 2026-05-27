"""
Program that shows various sequences.
"""

MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""
print(MENU)
menu_choice = int(input("Pick option (1 to 4): "))
while menu_choice != 4:
    if menu_choice == 1:
        x = int(input("Choice for x: "))
        y = int(input("Choice for y: "))
        if x % 2 == 0:  # If a number modulo 2 equals zero, then it's even.
            for i in range(x, y+1, 2):
                print(i, end=' ')  # The end=' ' adds a space
        else:
            for i in range(x+1, y+1, 2):
                print(i, end=' ')
        print()  # Goes to a new line.
    elif menu_choice == 2:
        x = int(input("Choice for x: "))
        y = int(input("Choice for y: "))
        if x % 2 != 0:  # If a number modulo 2 doesn't equal zero, then it's odd.
            for i in range(x, y+1, 2):
                print(i, end=' ')
        else:
            for i in range(x+1, y+1, 2):
                print(i, end=' ')
        print()
    elif menu_choice == 3:
        x = int(input("Choice for x: "))
        y = int(input("Choice for y: "))
        for i in range(x, y + 1, 1):
            print(i**2, end=' ')
        print()
    else:
        print("Invalid choice.")
    print(MENU)
    menu_choice = int(input(">>> "))
print("Exiting program.")
