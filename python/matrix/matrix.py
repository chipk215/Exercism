class Matrix:
    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")

    def check_index(self, index):
        max_rows = len(self.rows)
        if index < 1:
            raise ValueError(f"index {index} must be greater than 0.")
        if index > max_rows:
            raise ValueError(f"index {index} must be less than  than {max_rows}.")

    def row(self, index):
        self.check_index(index)
        return self.rows(index - 1)

    def column(self, index):
        if index < 1:
            raise ValueError(f"index {index} must be greater than 0.")
        col = []
        for row in self.rows:
            if index > len(row):
                raise ValueError(f"col index {index} invlaid for row {row}.")

            col.append(row[index - 1])

        return col
