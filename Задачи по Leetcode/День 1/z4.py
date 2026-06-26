# Задание 4

class Player:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health


    def take_damage(self, damage: int) -> None:
        if self.health - damage <=0:
            print("Игрок умер")
        else:
            self.health -= damage

    def heal(self, amount: int) -> None:
        if self.health + amount <=100:
            self.health += amount
        else:
            print("Здоровье не должно быть больше 100")

    def info(self):
        print(f"Name: {self.name}, Health: {self.health}")

p = Player("Alex", 100)

p.take_damage(30)
p.info()        # 70 HP

p.heal(20)
p.info()        # 90 HP

p.take_damage(200)  # Игрок умер

