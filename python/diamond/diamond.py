def rows(letter):
    
    number = ord(letter) - ord("A") + 1
    result_quarter = [[chr(j + ord("A")) if j == i else " " for j in range(number)] for i in range(number)]
    result_half = [result_quarter[i][-1:0:-1]+result_quarter[i] for i in range(number)]
    result = result_half + result_half[::-1][1:]
    
    return ["".join(i) for i in result]


