import re
def answer(question):
    question = question[:-1]
    text_err = [x for x in question.split(" ") if x.isalpha() and x not in ['What', 'is', 'plus', 'minus', 'multiplied', 'divided', 'by']]
    text_num = re.findall(r'What\sis\s(\d+)$', question)
    text_calc = re.findall(r'What\sis\s(-?\d+(?:\s(?:plus|minus|multiplied\sby|divided\sby)\s-?\d+)+)$', question)
    if text_err:
        raise ValueError("unknown operation")
    elif text_num:
        return int(text_num[0])
    elif text_calc:
        text_calc = text_calc[0].replace('plus', '+').replace('minus', '-').replace('multiplied by', '*').replace('divided by', '/').split(' ')
        result = ''
        for i in text_calc:
            result += i
            if i.isdigit() or (len(i) > 1 and i[1:].isdigit()):
                result = str(eval(result))
        return int(float(result))
    else:
        raise ValueError("syntax error")

