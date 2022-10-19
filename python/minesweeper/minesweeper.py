def annotate(minefield):
    adjacent_cells = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
    result = []
    for row in range(len(minefield)):
        if len(minefield[row]) != len(minefield[0]):
            raise ValueError("The board is invalid with current input.")
        result_row = []
        for column in range(len(minefield[row])):
            if minefield[row][column] not in [" ", "*"]:
                raise ValueError("The board is invalid with current input.")
            elif minefield[row][column] == "*":
                result_row.append("*")
                continue
            count = 0
            for cell in adjacent_cells:
                x = column + cell[0]
                y = row + cell[1]
                if 0 <= x < len(minefield[row]) and 0 <= y < len(minefield) and minefield[y][x] == "*":
                    count += 1
            result_row.append(str(count) if count else " ")
        result.append("".join(result_row))
    return result
