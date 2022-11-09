import math
def spiral_matrix(size):
    matrix = [['' for j in range(size)] for i in range(size)]
    number = 0
    line = 1
    while line <= math.ceil(size/2):
        turn = 0
        while turn < 4:
            for i in range(size):
                if not matrix[line-1][i]:
                    number += 1
                    matrix[line-1][i] = number
            matrix = [[*i] for i in zip(*[line[::-1] for line in matrix])]
            turn += 1
        line += 1
    return matrix
