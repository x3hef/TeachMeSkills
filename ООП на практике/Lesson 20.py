# Магические методы __getitem__ __setitem__ __delitem__

class Vector:
    def __init__(self, *args):
        self.value = list(args)

    def __repr__(self):
        return str(self.value)

    def __getitem__(self, item): # item - индекс
        if 0<item<len(self.value):
            return self.value[item]
        return False

    def __setitem__(self, key, value):
        if 0<key<len(self.value):
            self.value[key] = value
        return False

    def __delitem__(self, key):
        if 0<key<len(self.value):
            self.value.pop(key)