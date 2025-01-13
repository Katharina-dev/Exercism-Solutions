import math

def to_decimal(input_base, digits):
    result = []
    for pow, digit in enumerate(digits[::-1]):
        result.append(digit * input_base ** pow)
    return sum(result)

def from_decimal(digit, output_base):
    if not digit:
        return [0]
    result = []
    pow = round(math.log(digit, output_base))
    while pow >= 0:
        new_digit = digit//output_base**pow
        result.append(new_digit)
        digit -= new_digit*output_base**pow
        pow -= 1
    return result

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif [digit for digit in digits if digit < 0 or digit >= input_base]:
        raise ValueError("all digits must satisfy 0 <= d < input base")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    elif output_base == 10:
        return [int(i) for i in list(str(to_decimal(input_base, digits)))]
    elif input_base == 10:
        return from_decimal(int(''.join([str(i) for i in digits])), output_base)
    return from_decimal(to_decimal(input_base, digits), output_base)
