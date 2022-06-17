import re
def translate(text):
    return " ".join([trans_word(word) for word in text.split()])
    
def trans_word(word):
    trans = re.match(r'([euioa]|xr|yt)(\w+)|((?:[^euioaxyq](?!qu)|x(?!r)|y(?!t))[^euioaxyq]*)(\w+)|([^euioaxy]?qu)(\w+)|(q)([^u]+)', word)
    for i in range(1,9,2):
        if trans.group(1) and i == 1:
            return f'{trans.group(1)}{trans.group(2)}ay'
        elif trans.group(i):
            return f'{trans.group(i+1)}{trans.group(i)}ay'



