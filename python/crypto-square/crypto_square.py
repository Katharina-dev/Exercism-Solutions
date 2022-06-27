def cipher_text(plain_text):
    if plain_text == "":
        return ""
    plain_text = [i.lower() for i in plain_text if i.isalnum()]
    r = int(len(plain_text)**0.5)
    c = r if len(plain_text)**0.5 == r else r+1
    r = r if r*c >= len(plain_text) else r+1
    rectangle = []
    for i in range(0,r*c,c):
        rectangle.append(plain_text[i:i+c])
    if len(rectangle[0]) != len(rectangle[-1]):
        rectangle[-1].extend([' ']*(len(rectangle[0])-len(rectangle[-1])))
    coded = list(zip(*rectangle))
    return ' '.join(''.join(item) for item in coded)


