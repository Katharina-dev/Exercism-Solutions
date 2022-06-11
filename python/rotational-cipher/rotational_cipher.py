def rotate(text, key):
    result = []
    for l in text:
        if l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            l = chr((ord(l.lower()) - 97 + key)%26 + 97).upper()
        elif l in "abcdefghijklmnopqrstuvwxywz":
            l = chr((ord(l) - 97 + key)%26 + 97)
        result.append(l)
    return "".join(result)


