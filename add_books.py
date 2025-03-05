from load_books import load_books
from save_books import save_books

def add_books():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN or Book ID: ")
    genre = input("Enter book genre: ")
    price = input("Enter book price: ")
    quantity = input("Enter quantity in stock: ")

    if not title.strip():
        print("Error: Title cannot be empty.")
        return
    if not price.replace('.', '', 1).isdigit() or float(price) <= 0:
        print("Error: Price must be a positive number.")
        return
    if not quantity.isdigit() or int(quantity) < 0:
        print("Error: Quantity must be a non-negative integer.")
        return

    for book in books:
        if book["isbn"] == isbn:
            print("Error: A book with this ISBN already exists.")
            return

    books.append({
        "title": title,
        "author": author,
        "isbn": isbn,
        "genre": genre,
        "price": float(price),
        "quantity": int(quantity)
    })
    save_books(books)
    print("Book added successfully!")
