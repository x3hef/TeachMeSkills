# Задание 10

class Timer:
    def __init__(self, seconds: int):
        self._seconds = seconds

    @property
    def second(self):
        return self._seconds

    @second.setter
    def second(self, seconds: int):

        if seconds < 0:
            print("Нельзя ставить отрицательное!")
        else:
            self._seconds = seconds

    def tick(self):
        if self._seconds - 1 <= 0:
            self._seconds = 0
        else:
            self._seconds -= 1


    def add_seckonds(self, add):
        self._seconds += add


    @staticmethod
    def time(sec):
        return sec >=0
