def classify(number):
    
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    elif number == 1:
        result = 'deficient'
        
    else:
        lst = {1}
        for i in range(2,int(number**0.5)+1):
            if number%i == 0:
                lst.add(i)
                lst.add(int(number/i))
        if sum(lst) == number:
            result = 'perfect'
        elif sum(lst) > number:
            result = 'abundant'
        elif sum(lst) < number:
            result = 'deficient'
            
    return result



