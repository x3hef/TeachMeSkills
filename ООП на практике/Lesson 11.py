# classmethod и staticmethod

class Exsmple:
    def hello(self):
        print("Hello World")

    def instaqnse_hello(self):
        print(f"{self}")


    @staticmethod
    def statick_hello():
        print("Statick Hello World")

    @classmethod
    def instaqnse_hello2(cls):
        print(f"{cls}")

print(Exsmple.statick_hello())
y = Exsmple()
y.hello()
y.instaqnse_hello()
y.statick_hello()
y.instaqnse_hello2()
print(Exsmple.statick_hello())
