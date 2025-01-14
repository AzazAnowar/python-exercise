"""
 Define a Library class to manage books using attributes like title, author,
and availability. Include methods to borrow and return books, tracking the
availability status
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return f"You have borrowed '{title}'"
        return "Book not available"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                return f"You have returned '{title}'"
        return "Book not found"

# Example usage:
library = Library()
library.add_book(Book("Python Programming", "Author A"))
library.add_book(Book("Data Science", "Author B"))
print(library.borrow_book("Python Programming"))
print(library.return_book("Python Programming"))