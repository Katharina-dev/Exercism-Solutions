color_bands = {'black': '0', 'brown': '1', 'red': '2',
               'orange': '3', 'yellow': '4', 'green': '5',
               'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
tolerance = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%',
             'green': '0.5%', 'brown': '1%', 'red': '2%',
             'gold': '5%', 'silver': '10%'}
def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    two_figures = color_bands[colors[0]] + color_bands[colors[1]]
    figures = two_figures if len(colors) == 4 else two_figures + color_bands[colors[2]]
    number = int(figures + int(color_bands[colors[-2]])*'0')
    
    if number//1000000000 > 0:
        prefix = 'giga'
        rest = number%1000000000
        number //= 1000000000
    elif number//1000000 > 0:
        prefix = 'mega'
        rest = number%1000000
        number //= 1000000
    elif number//1000 > 0:
        prefix = 'kilo'
        rest = number%1000
        number //= 1000
    else:
        prefix = ''
        rest = ''
    rest = '.' + str(rest).rstrip('0') if rest else ''
    return f'{number}{rest} {prefix}ohms ±{tolerance[colors[-1]]}'
