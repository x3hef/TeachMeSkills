from datetime import datetime

#################################################################################################

# Задание 1

class GameCharacter:
    def __init__(self, name: str, health: int, level: int):
        self.name = name
        self.__health = health
        self.level = level

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 100:
            self.__health = 100
        elif value < 0:
            self.__health = 0
        else:
            self.__health = value

    def _level_up(self):
        self.level += 1

    def attack(self, other_character):
        other_character.health -= 10

    @classmethod
    def person(cls, name):
        return cls(name, 100, 1)

    @staticmethod
    def con_level():
        return 2

    @staticmethod
    def com_level(hero1, hero2):
        if hero1.lavel > hero2.level:
            return hero1
        elif hero1.level < hero2.level:
            return hero2
        else:
            return hero1, hero2, "Уровни равные"


#################################################################################################

# Задание 2

class Store:
    def __init__(self, name_store: str, products: list):
        self.name_store = name_store
        self.products = products

    def add_products(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)

    def remove_products(self, name):
        for product in self.products:
            if name == product["name"]:
                self.products.remove(product)
                break

    def update_price(self, name, new_price):
        for product in self.products:
            if product["name"] == name:
                product["price"] = new_price
                return "Цена обновлена"
        return "Товар не найден"

    def sell_product(self, name, quantity):
        for product in self.products:
            if product["name"] == name:

                if product["quantity"] >= quantity:
                    product["quantity"] -= quantity
                    return "Sell"
                else:
                    return "No count"
        return "Товар не найден"

    def get_inventory(self):
        inventory = []
        for product in self.products:
            inventory.append({
                "name": product["name"],
                "quantity": product["quantity"],
            })
        return inventory

    def find_most_expensive(self):
        if not self.products:
            return "Список пуст"

        most_expensive = self.products[0]
        for product in self.products:
            if product["price"] > most_expensive["price"]:
                most_expensive = product

        return most_expensive

    def find_cheapest(self):
        if not self.products:
            return "Список пуст"
        cheapest = self.products[0]
        for product in self.products:
            if product["price"] < cheapest["price"]:
                cheapest = product
        return cheapest


#################################################################################################

# Задание 3

class Book:
    def __init__(self,name: str, author: str, year_of_publication: int, status: str):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication
        self.status = status

        try:
            if status not in ["в библиотеке", "выдана"]:
                raise ValueError(f" Неверный статус!")

            self.status = status

        except ValueError as error:
            print(error)
            self.status = "в библиотеке"

    def info(self):
        a = "*"
        return (f" {a * 20}\n "
                f"Название: {self.name}\n "
                f"Автор: {self.author};\n "
                f"Год издания: {self.year_of_publication};\n "
                f"Статус: {self.status}\n {a * 20} ")

    def  mark_as_taken(self, status):
        if self.status == "в библиотеке":
            self.status = "выдана"

        return self.status


    def  mark_as_returned(self, status):
        if self.status == "выдана":
            self.status = "в библиотеке"

        return self.status


class Library:
    def __init__(self,name_library: str, list_book: list):
        self.name_library = name_library
        self.list_book = list_book

    def add_book(self, book: Book):
        self.list_book.append(book)
        return self.list_book

    def remove_book(self, book):
        if book in self.list_book:
            self.list_book.remove(book)
            return  "Book removed"
        else:
            return "Book not found"

#################################################################################################

# Задание 4

class Wallet:
    def __init__(self, balance: float):
        self._balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            return f"Пополнение на {amount}"
        return "Некоректная сумма!"

    def withdraw(self, amount: float):
        if amount > self._balance:
            return "Недостаточно средств"
        elif amount < 0:
            return "Некоректная сумма"
        else:
            self._balance -= amount
            return f"Снятие средств {amount}"

    def transfer_to(self, other_wallet, amount: float):
        if amount > self._balance:
            return "Недостаточно средств"
        elif amount <= 0:
            return "Некор сумма"
        else:
            self._balance -= amount
            other_wallet += amount
            return "Перевод выполнен!"

    def __apply_bonus(self):
        self._balance *= 1.01

    @property
    def balance(self):
        return self._balance

    @staticmethod
    def wallet_balance(wallet):
        return wallet.balance

#################################################################################################

# Задание 6

class Car:
    def __init__(self, brand: str, model: str, year: int, fuel_level: int, mileage: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.mileage = mileage

    def drive(self, distance):
        fuel_needed = distance * 0.1

        if fuel_needed > self.fuel_level:
            return "Недостаточно топлива"

        self.mileage += distance
        self.fuel_level -= fuel_needed

        return f"Машина проехала {distance} км"

    def refuel(self, liters):
        if liters > 0:
            self.liters += liters
            return f"Заправлено {liters} liters"
        return "Некоректное действие"

    def info(self):
        return (f"{self.brand} {self.model}, {self.year} год | "
                f"Топливо: {round(self.fuel_level, 2)} л | "
                f"Пробег: {self.mileage} км")

    def __check_fuel(self, distance):
        full_distance = distance * 0.1
        return self.fuel_level >= full_distance

    def age(self):
        current_year = datetime.now().year
        return current_year - self.year

    @classmethod
    def from_string(cls, data):
        brand, model, year = data.split(", ")
        return cls(brand, model, int(year), 0, 0)


#################################################################################################

# Задание 7

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, weight, value):
        item = {
            "name": name,
            "weight": weight,
            "value": value
        }
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return "Item removed"
            return "Item not found"
        return False

    def get_total_weight(self):
        return sum(item["weight"] for item in self.items)

    def get_total_value(self):
        return sum(item["value"] for item in self.items)

    def find_heaviest(self):
        if not self.items:
            return False
        return max(self.items, key=lambda item: item["weight"])

    def find_most_valuable(self):
        if not self.items:
            return False
        return max(self.items, key=lambda item: item["value"])

    def sort_by_value(self, descending=True):
        return sorted(self.items, key=lambda x: x["value"], reverse=descending)

    def sort_by_weight(self, descending=True):
        return sorted(self.items, key=lambda x: x["weight"], reverse=descending)

