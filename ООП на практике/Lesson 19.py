


class Coutnter:
    def __init__(self):
        counter = 0
        print("cal __init__")

    def __call__(self, *args, **kwargs):
        self.counter +=1
        print("cal __call__")


print(Coutnter().__call__)