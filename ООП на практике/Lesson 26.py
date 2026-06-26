

class Person:
    def life(self):
        print("life")

    def sleep(self):
        print("sleep")

    def combo(self):
        self.life()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()

class Doctor(Person):
    def sleep(self):
        print("sleep")



f = Doctor()
f.life()
f.sleep()
f.combo()