def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]
    triangle = rows(row_count - 1)
    added_numbers = []
    if len(triangle[-1]) > 1:
        for i in range(1,len(triangle[-1])):
            added_numbers.append(triangle[-1][i-1]+triangle[-1][i])
    return triangle + [[1] + added_numbers + [1]]
