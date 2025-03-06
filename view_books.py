from load_books import load_books

def view_books():
    books = load_books()
    if not books:
        print("No Books Available Right Now")
        return
    
    total_books = len(books)
    index = 1
    for book in books:
        if index == 1:
            print(f"\nAll Book List({total_books}):\n")
        print(f"{index}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: ৳{book['price']}, Stock: {book['quantity']}")
        index += 1