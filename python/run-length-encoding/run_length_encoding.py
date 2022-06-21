import re

def decode(string):
    if string == "":
        return ""
    #divide the string
    string = re.split(r'( +)', re.sub(r'\d+\b', ' ', string))
    result = []
    for item in string:
        #remove insignificant digits
        lst = [i for i in re.findall(r'\d*\w|\s', item) if not i.isdigit()]
        #calculate the number of letters
        lst = [int(item[:-1])*item[-1] if len(item)>1 else item[-1] for item in lst]
        lst = ''.join(lst)
        if lst:
            result.append(lst)
    return  ''.join(result) if len(result) > 1 else result[0]


def encode(string):
    if string == "":
        return ""
    lst = []
    #number of equal letters
    count_l = 1
    letter = string[0]
    for i in range(1,len(string)):
        if letter == string[i]:
            count_l += 1
        else:
            if count_l != 1:
                lst.append(str(count_l))
            lst.append(letter)
            letter = string[i]
            count_l = 1
    if count_l != 1:
        lst.append(str(count_l))
    lst.append(letter)
    return ''.join(lst)


