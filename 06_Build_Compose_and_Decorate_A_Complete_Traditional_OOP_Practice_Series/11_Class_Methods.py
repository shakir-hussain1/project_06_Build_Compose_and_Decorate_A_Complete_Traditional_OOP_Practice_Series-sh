class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment book count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_book_count(cls):
        print(f"Total books: {cls.total_books}")

# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Display the total number of books
Book.display_book_count()
