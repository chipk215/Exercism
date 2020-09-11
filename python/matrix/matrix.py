class Matrix:
    def __init__(self, matrix_string):
        strings = matrix_string.split("\n")
        self.rows = [[int(item) for item in row] for row in [string_value.split() for string_value in strings]]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        col = []
        for row in self.rows:
            col.append(row[index - 1])

        return col
