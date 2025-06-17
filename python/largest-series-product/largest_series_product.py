import math

def largest_product(series, size):
    
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    elif not all(item.isdigit() for item in series):
        raise ValueError("digits input must only contain digits")
        
    larg_prod = 0
    
    for i in range(len(series)-size+1):
        prod = math.prod([int(item) for item in series[i:i+size]])
        if prod > larg_prod:
            larg_prod = prod
        
    return larg_prod
