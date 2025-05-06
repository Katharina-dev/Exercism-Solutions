def primes(limit):

    marked = set()
    
    for number in range(2, limit+1):
            
        if number**2 <= limit and number not in marked:
            marked.update([i for i in range(number**2, limit+1,number)])

    return sorted(set(range(2, limit+1)) - marked)
