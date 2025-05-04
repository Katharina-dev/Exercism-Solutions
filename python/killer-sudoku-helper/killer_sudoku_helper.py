import itertools


def combinations(target, size, exclude):
    
    arrays = [list(map(int, array)) for array in itertools.combinations('123456789', size)]
    combs = []
    
    for array in arrays:
        for item in array:
            if item in exclude or sum(array) != target:
                break
        else:
            combs.append(array)
            
    return combs
