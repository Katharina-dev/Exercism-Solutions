numbers = {1: "one",
           2: "two",
           3: "three",
           4: "four",
           5: "five",
           6: "six",
           7: "seven",
           8: "eight",
           9: "nine",
           10: "ten",
           11: "eleven",
           12: "twelve",
           13: "thirteen",
           14: "fourteen",
           15: "fifteen",
           16: "sixteen",
           17: "seventeen",
           18: "eighteen",
           19: "nineteen",
           20: "twenty",
           30: "thirty",
           40: "forty",
           50: "fifty",
           60: "sixty",
           70: "seventy",
           80: "eighty",
           90: "ninety",
           100: "hundred",
           1000: "thousand",
           1000000: "million",
           1000000000: "billion"}

def say_basic_10(number):
    if number == 0:
        return ""
    elif int(str(number).lstrip("0")) in numbers:
        return numbers[number]
    else:
        return f'{numbers[number//10*10]}-{numbers[number%10]}'
    
def say_basic_100(number):
    if number < 100:
        return say_basic_10(number)
    basic_10 = say_basic_10(number%100)
    return f'{numbers[number//100]} hundred {basic_10}'

def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    elif number == 0:
        return "zero"
    elif number == 100 or number == 1000 or number == 1000000 or number == 1000000000:
        return f'one {numbers[number]}'
    elif number < 1000:
        return say_basic_100(number)
    result = []
    if number//1000000000 != 0:
        result.append(say_basic_100(number//1000000000))
        result.append(numbers[1000000000])
        number -= number//1000000000*1000000000
    if number//1000000 != 0:
        result.append(say_basic_100(number//1000000))
        result.append(numbers[1000000])
        number -= number//1000000*1000000
    if number//1000 != 0:
        result.append(say_basic_100(number//1000))
        result.append(numbers[1000])
        number -= number//1000*1000
    result.append(say_basic_100(number))
    return ' '.join(result)


