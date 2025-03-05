from load_books import load_books
from save_books import save_books

def remove_book():
    books = load_books()
    isbn = input("Enter ISBN of the book to remove: ")
    books = [book for book in books if book["isbn"] != isbn]
    save_books(books)
    print("Book removed successfully!")
