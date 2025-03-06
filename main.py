from add_books import add_books
from view_books import view_books
from remove_book import remove_book
from search_book import search_book

def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_books()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Exit..")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()