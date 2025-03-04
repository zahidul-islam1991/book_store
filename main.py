def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("Add Book")
        elif choice == "2":
            print("View All Books")
        elif choice == "3":
            print("Delete Book")
        elif choice == "4":
            print("Exit..")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()