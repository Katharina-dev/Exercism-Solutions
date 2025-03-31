class StackUnderflowError(Exception):
    
    def __init__(self, message):
        self.message = message

        
def standard_evaluate(string):
    
    data = [symbol.lower() for symbol in string.split()]
    stack = []
    for symbol in data:
        if symbol.isalpha() and symbol not in 'dupdropswapover':
            raise ValueError("undefined operation")
        elif symbol not in '+-*/dupdropswapover':
            stack.append(int(symbol))
            continue
        elif len(stack) < 1 or len(stack) < 2 and symbol in '+-*/swapover':
                raise StackUnderflowError("Insufficient number of items in stack")
        elif symbol == 'dup':
            stack.append(stack[-1])
        elif symbol == 'drop':
            stack.pop()
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if symbol == '+':
                stack.append(num1 + num2)
            elif symbol == '-':
                stack.append(num2 - num1)
            elif symbol == '*':
                stack.append(num1 * num2)
            elif symbol == '/':
                if num1 == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(num2 // num1)
            elif symbol == 'swap':
                stack.extend([num1, num2])
            elif symbol == 'over':
                stack.extend([num2, num1, num2])
    return stack


def evaluate(input_data):
    
    if len(input_data) == 1:
        if input_data[0][0] == ':':
            raise ValueError("illegal operation")
        return standard_evaluate(input_data[0])
    dict = {}
    for item in input_data:
        item = item.lower()
        if item[0] == ':':
            words = item[1:-1].split()
            dict[words[0]] = dict[words[1:][0]] + words[2:] if words[1:][0] in dict else words[1:]
        else:
            for key in dict.keys():
                if key in item:
                    modif_item = item.replace(key, ' '.join(dict[key]))
                    item = modif_item
            return standard_evaluate(item)
