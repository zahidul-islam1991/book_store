from load_books import load_books

def search_book():
    books = load_books()
    if not books:
        print("No books available.")
        return

    isbn = input("Enter ISBN: ").strip()
    for book in books:
        if book["isbn"] == isbn:
            print("\nBook Found:\n")
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: ${book['price']}, Stock: {book['quantity']}")
            return

    print("\nBook not found😞")