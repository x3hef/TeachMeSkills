# Задание 7


class Book:
    def __init__(self, title: str, author: str, available: str):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available < 0:
            print("Книга недоступна")
        else:
            self.available -= 1

    def return_book(self):
        self.available += 1


    def info(self):
        print(f"{self.title}, {self.author}, {self.available}")


