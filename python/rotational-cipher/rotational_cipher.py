letters = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    
    rotated_letters = letters[key:] + letters[:key]
    trans = str.maketrans(letters + letters.upper(), rotated_letters + rotated_letters.upper())
    
    return text.translate(trans)

