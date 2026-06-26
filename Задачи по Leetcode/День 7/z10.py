# Задание 10

class Character:
    def __init__(self, name, health):
        self.name = name
        self._health = health

    @property
    def health(self):
        return self._health

    def take_damage(self, amount):
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            print(f"{self.name} погиб!")

    def heal(self, amount):
        self._health += amount
        if self._health > 100:
            self._health = 100

    def info(self):
        print(f"{self.name}: Здоровье {self._health}")


class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self, cost):
        if cost > self.mana:
            print("Не хватает маны!")
        else:
            self.mana -= cost

    def info(self):
        print(f"{self.name}: Здоровье {self._health}, Мана {self.mana}")
