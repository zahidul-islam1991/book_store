from load_books import load_books

def search_book():
    books = load_books()
    if not books:
        print("No books available.")
        return

    search_term = input("Enter ISBN, Title, Author, or Genre: ").strip().lower()

    results = [
        book for book in books 
        if search_term in book["isbn"].lower()
        or search_term in book["title"].lower()
        or search_term in book["author"].lower()
        or search_term in book["genre"].lower()
    ]

    total_books = len(results)
    index = 1
    if results:
        for book in results:
            if index == 1:
                print(f"\nTotal Matched Books Found({total_books}):\n")
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: ৳{book['price']}, Stock: {book['quantity']}")
            index += 1 
    else:
        print("\nNo matching books found 😞")
