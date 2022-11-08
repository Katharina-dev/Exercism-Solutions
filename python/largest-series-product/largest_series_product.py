import math
def largest_product(series, size):
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    elif [i for i in series if i not in '0123456789']:
        raise ValueError("digits input must only contain digits")
    larg_prod = 0
    for i in range(len(series)-size+1):
        prod = math.prod([int(i) for i in series[i:i+size]])
        larg_prod = prod if prod > larg_prod else larg_prod
    return larg_prod
