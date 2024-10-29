'''scnario: managing the inventory of a book library, including available books and borrowed books.
tasks:
1. create a list of dictionaries, where each dictionary contains "title" and "author" and "isbn" and "borrowed"(True/False) 
2. add new book to the library
3. update the status of a book as borrowed or returned
4. remove a book that no longer aviailable
5. find book by a particular author
6. use a set to keep track pf unique borrowers who have borrowed books from the library
7. display the list of books in the library
'''

# Initial list of books
library_books = [
    {"title": "Book A", "author": "Author 1", "isbn": "123", "borrowed": False},
    {"title": "Book B", "author": "Author 2", "isbn": "456", "borrowed": False},
    {"title": "Book C", "author": "Author 1", "isbn": "789", "borrowed": True}
]


# Set to track unique borrowers
unique_borrowers = set()
unique_borrowers.add("Borrower 1")

while True:
    print("\nLibrary Management System Menu")
    print("1. Add a new book")
    print("2. Update the status of a book")
    print("3. Remove a book")
    print("4. Find books by a particular author")
    print("5. Display the list of books")
    print("6. Display unique borrowers")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        new_book = {"title": title, "author": author, "isbn": isbn, "borrowed": False}
        library_books.append(new_book)
        print(f"Added book: {title}")
    elif choice == '2':
        isbn = input("Enter the ISBN of the book: ")
        status = input("Enter the status (borrowed/returned): ").lower()
        borrowed = status == "borrowed"
        for book in library_books:
            if book["isbn"] == isbn:
                book["borrowed"] = borrowed
                print(f"Updated status of book with ISBN {isbn}")
                break
        else:
            print(f"Book with ISBN {isbn} not found")
    elif choice == '3':
        isbn = input("Enter the ISBN of the book to remove: ")
        library_books = [book for book in library_books if book["isbn"] != isbn]
        print(f"Removed book with ISBN {isbn}")
    elif choice == '4':
        author = input("Enter the author to search for: ")
        books_by_author = [book for book in library_books if book["author"] == author]
        print(f"Books by {author}: {books_by_author}")
    elif choice == '5':
        for book in library_books:
            print(book)
    elif choice == '6':
        print("Unique borrowers:")
        for borrower in unique_borrowers:
            print(borrower)
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")