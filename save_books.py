import json

BOOKS_FILE = "books.json"

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)
