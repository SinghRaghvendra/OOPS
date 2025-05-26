# Setup
library = Library()
book1 = Book("1984", "George Orwell", "123")
book2 = Book("Python Basics", "Jane Doe", "456")
library.add_book(book1)
library.add_book(book2)

user = User("Alice")


library.list_books()

user.borrow_book(book1)
user.borrow_book(book2)

library.list_books()

user.return_book(book1)
library.list_books()



