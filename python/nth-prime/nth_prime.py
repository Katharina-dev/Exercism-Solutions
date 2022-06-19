def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    prime_numbers = [2]
    n = 2
    while len(prime_numbers) != number:
        n += 1
        for i in prime_numbers:
            if n%i == 0:
                break
        else:
            prime_numbers.append(n)
    return prime_numbers[-1]


