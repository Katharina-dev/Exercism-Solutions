import re

def abbreviate(words):
    
    return ''.join([i[0].upper() for i in re.findall(r'[A-Za-z\']+', words)])
