from load_books import load_books

def view_books():
    books = load_books()
    if not books:
        print("No Books Available Right Now")
        return
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: ${book['price']}, Stock: {book['quantity']}")