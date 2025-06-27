# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        print("Books in Library:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book} [{status}]")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
                return
        print("Book not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
                return
        print("You can't return this book.")

# User class (inherits from Library, for simplicity)
class User(Library):
    def __init__(self, name):
        super().__init__()  # Inherit Library's book list
        self.name = name

    # Method override (just adding user name info)
    def borrow_book(self, title):
        print(f"{self.name} is trying to borrow a book...")
        super().borrow_book(title)

    def return_book(self, title):
        print(f"{self.name} is trying to return a book...")
        super().return_book(title)

# Example usage
# Creating books
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("1984", "George Orwell")

# Creating a library
my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Creating a user
user1 = User("Alice")
user1.books = my_library.books  # Share the same book list

# Simulate actions
user1.view_books()
user1.borrow_book("Harry Potter")
user1.view_books()
user1.return_book("Harry Potter")
user1.view_books()
