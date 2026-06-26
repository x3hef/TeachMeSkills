# Задание 10

class Library:
    def __init__(self, books: list):
        self.books = books

    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        self.books.remove(book)

    def show_books(self):
        for book in self.books:
            print(book)
