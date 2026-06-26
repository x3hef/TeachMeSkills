# Задание 1

class Weapon:
    def __init__(self, name: str, damage: int, durability: int):
        self.name = name
        self.damage = damage
        self.durability = durability

    def attack(self, value):
        if self.durability <= 0:
            print("Оружие уже сломано!!!")
        if self.durability - value <= 0:
            print("Оружие сломалось")
        else:
            self.durability -= value

    def info(self):
        print(f"Имя оружия: {self.name}"
              f"Урон оружия: {self.damage}"
              f"Прочность: {self.durability}")

class Player:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.weapon = None  # текущее оружие

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} экипировал {weapon.name}")

    def attack(self):
        if not self.weapon:
            print(f"{self.name} не имеет оружия!")
            return
        damage = self.weapon.attack()
        print(f"{self.name} атакует {self.weapon.name}, урон: {damage}")

    def take_damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} погиб!")
        else:
            print(f"{self.name} получил {amount} урона, здоровье: {self.health}")

    def info(self):
        weapon_name = self.weapon.name if self.weapon else "нет оружия"
        print(f"Игрок: {self.name}, Здоровье: {self.health}, Оружие: {weapon_name}")


