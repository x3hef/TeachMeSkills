# Пространство имен

class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 2
    REACT_DEV = 1

    def info(self):
        print(self.PYTHON_DEV)
        print(self.GO_DEV)

    def make_backand(self):
        print("Python and Go")

    def make_frontend(self):
        print("React")



iti = DepartmentIT()
iti.info()