# Полиморфизм


class Building:
    year = None
    city = None
    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print(self.year, self.city)


class School(Building):
    pupils = 0

    def __init__(self, pupils, city, year):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print("pupils", self.pupils)



school = School(5, 5002, "dsd")
print(school.get_info())