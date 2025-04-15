import re

def is_valid(isbn):
    
    letters = re.findall(r'[A-Wa-wYZyz]', isbn)
    if letters:
        return False
    figures = re.findall(r'[0-9X]', isbn)
    if len(figures) != 10:
        return False
    if 'X' in figures and figures.index('X') != 9:
        return False
    figures[9] = '10' if figures[9] == 'X' else figures[9]
    figures = figures[::-1]
    
    return not sum([int(figures[i-1])*i for i in range(1,11)])%11
