class Book:

  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year


class Library:

  def __init__(self):
    self.books = []

  def add_book(self, title, author, year):
    book = Book(title, author, year)
    self.books.append(book)
    print(f"Added book: {title} by {author} ({year})")

  def search_book(self, keyword):
    matching_books = []
    for book in self.books:
      if keyword.lower() in book.title.lower() or keyword.lower(
      ) in book.author.lower():
        matching_books.append(book)

    if len(matching_books) == 0:
      print("No matching books found.")
    else:
      print(f"Matching books for '{keyword}':")
      for book in matching_books:
        print(f"- {book.title} by {book.author} ({book.year})")

  def display_books(self):
    if len(self.books) == 0:
      print("No books in the library.")
    else:
      print("Books in the library:")
      for book in self.books:
        print(f"- {book.title} by {book.author} ({book.year})")


# Creating a library instance
library = Library()

# Adding books to the library
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
library.add_book("1984", "George Orwell", 1949)
library.add_book("Pride and Prejudice", "Jane Austen", 1813)
library.add_book("The Catcher in the Rye", "J.D. Salinger", 1951)

# Searching for books
library.search_book("1984")
library.search_book("Harry Potter")

# Displaying all books
library.display_books()
