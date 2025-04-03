def square_root(number):
    
    if number < 2:
        return number if number else 0
        
    start = 0
    end = number
    
    while start <= end:
        middle = (start + end)//2
        if middle * middle == number:
            return middle
        elif middle * middle < number:
            result = middle
            start = middle + 1
        else:
            end = middle-1
            
    return result
