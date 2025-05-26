class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True  # Initially, the book is available
        
        
        
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {'Available' if self.is_available else 'Checked Out'}"
    
    
class User:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is currently checked out.")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")
            
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book.title} from the library.")

    def list_books(self):
        print("\nBooks in the library:")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.title} ({status})")


print("Library system initialized.")
print("Welcome to AI COUNCEL LIBRARY")


            
import os
print(os.listdir())