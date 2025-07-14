def flatten(iterable):
    
    result = [i.strip() for i in str(iterable).replace("[","").replace("]","").split(",")]
    
    return [int(i) for i in result if i not in ("None", "")]


