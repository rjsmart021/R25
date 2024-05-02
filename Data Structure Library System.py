def add_book(library, title, author):
    new_book = (title, author)
    
    # Check for duplicates
    for book in library:
        if new_book == book:
            print(f"The book '{title}' by {author} is already in the library.")
            return library
    
    # If not a duplicate, add the new book to the library
    library.append(new_book)
    print(f"The book '{title}' by {author} has been added to the library.")
    return library

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add new books to the library
library = add_book(library, "1984", "George Orwell")  # Duplicate book
library = add_book(library, "Animal Farm", "George Orwell")  # New book
library = add_book(library, "To Kill a Mockingbird", "Harper Lee")  # New book
library = add_book(library, "Animal Farm", "George Orwell")  # Duplicate book
library = add_book(library, "Life of Animals", "Reggie")  # New book

print("Updated Library:")
for i, book in enumerate(library, 1):
    print(f"Book {i}: '{book[0]}' by {book[1]}")
