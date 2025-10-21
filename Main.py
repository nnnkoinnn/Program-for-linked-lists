import Singly, Circ, Doubly

main_menu = [
    "1. Singly linked-list",
    "2. Circular linked-list",
    "3. Doubly linked-list",
    "4. Exit"
]

try:
    while True:
        print("=====MAIN=MENU=====")
        print()
        for options in main_menu:
            print(options)
        choice = int(input("Choose: "))
        match(choice):
            case 1:
                Singly.singly_menu()
            case 2:
                Circ.circular_menu()
            case 3:
                Doubly.doubly_menu()
            case 4:
                break
except ValueError as e:
    print(f"Error: {e}")