figures = {'0': [" _ ", "| |", "|_|", "   "],
           '1': ["   ", "  |", "  |", "   "],
           '2': [" _ ", " _|", "|_ ", "   "],
           '3': [" _ ", " _|", " _|", "   "],
           '4': ["   ", "|_|", "  |", "   "],
           '5': [" _ ", "|_ ", " _|", "   "],
           '6': [" _ ", "|_ ", "|_|", "   "],
           '7': [" _ ", "  |", "  |", "   "],
           '8': [" _ ", "|_|", "|_|", "   "],
           '9': [" _ ", "|_|", " _|", "   "]
    }


def convert(input_grid):
    
    if len(input_grid)%4:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line)%3:
            raise ValueError("Number of input columns is not a multiple of three")

    result = []
    for i in range(len(input_grid)//4):
        res = []
        for j in range(len(input_grid[i])//3):
            fig = [input_grid[i*4+k][j*3:j*3+3] for k in range(4)]
            figure = [i for i in figures if figures[i] == fig]
            if figure:
                res.append(figure[0])
            else:
                res.append('?')
        result.append(''.join(res))
        
    return ','.join(result) if len(result) > 1 else result[0]
