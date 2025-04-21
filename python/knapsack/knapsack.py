def maximum_value(maximum_weight, items):
    
    table = [[0 for weight in range(maximum_weight+1)] for item in range(len(items)+1)]
    
    for i in range(len(items)+1):
        for j in range(maximum_weight+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif items[i-1]['weight'] <= j:
                table[i][j] = max(items[i-1]['value'] + table[i-1][j-items[i-1]['weight']], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
                
    return table[-1][-1]
