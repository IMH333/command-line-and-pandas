def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1.Greet User")
        print("2. Show Info")
        print("3. Exit")

        choice = input("Enter your choice (1-3)")

        if choice == "1":
            print("hello, there!")
        elif choice == "2":
            print("This is a sample CLI tool")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Please enter 1, 2, or 3")

main_menu()