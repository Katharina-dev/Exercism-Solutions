def is_paired(input_string):
    
    opened = "[{("
    closed = "]})"
    lst = []
    
    for i in input_string:
        if i in opened:
            lst.append(i)
        elif i in closed:
            if not lst or opened[closed.index(i)] != lst.pop():
                return False
            
    return not lst
                
                
