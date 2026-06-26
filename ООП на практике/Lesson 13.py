# Магические методы - str - repr

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The name is - {self.name}"

    def __str__(self):
        return f"The name is - {self.name}"


s = Lion("Lion")
print(s)



