def saddle_points(matrix):
    def check_regular_matrix():
        row_length = len(matrix[0])
        if not all([len(r) == row_length for r in matrix]):
            raise ValueError("Irregular matrix")

    def get_column(c):
        return [r[c] for r in matrix]

    if len(matrix) == 0:
        return []

    check_regular_matrix()
    saddle_point_coords = []
    for row_num, row in enumerate(matrix):
        max_row_value = max(row)
        for col, value in enumerate(row):
            if value == max_row_value:
                column = get_column(col)
                if value == min(column):
                    saddle_point_coords.append({"row": row_num+1, "column": col+1})

    return saddle_point_coords
