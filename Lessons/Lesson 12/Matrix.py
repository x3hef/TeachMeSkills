

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def share(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        return rows, cols

