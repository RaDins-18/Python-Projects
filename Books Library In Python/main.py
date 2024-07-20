# QUESTION:

# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program does not persist the books after the program is stopped!



# SOLUTION:

# Library Class.
class Library:
    # __init__ constructor for assinging number of books and books.
    def __init__(self):
        self.no_of_books = 0
        self.books = {}
    
    # print_books function for print all books in the library.
    def print_books(self):
        print("Books:")
        # For loop for getting each book and category of book.
        for book, category in self.books.items():
            print(f"-  {book}  (Category: {category})")
    
    # add_book function add a book in the library and increase number of books.
    def add_book(self, book, category):
        # Add book with its category.
        self.books[book] = category
        # Increase no of books.
        self.no_of_books += 1
    
    # get_no_of_books function returns total number of books.
    def get_no_of_books(self):
        return self.no_of_books

# Create a library object by Library class.
library = Library()
library.add_book("Harry Potter", "Fiction")

# Show the initial number of books.
print("Initial number of books:", library.get_no_of_books())

# While True for running continuously unless program is quit.
while True:
    # Show enter book name message and tells info about program.
    print("Enter a book name (Enter 'q' to quit and get the total info):")
    # Gets book name.
    book = str(input())
    # If user input is q then break the loop and stops program.
    if book == 'q':
        break
    # Show enter category of book message.
    print("Enter the category of the book:")
    # Get category of book.
    category = input()
    # Add book and its category to the library object.
    library.add_book(book, category)

# Show the final number of books.
print("Final number of books:", library.get_no_of_books())

# Print all books in the library object.
library.print_books()