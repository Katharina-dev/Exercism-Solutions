letters = "abcdefghijklmnopqrstuvwxyz"
e_letters = letters[::-1]


def encode(plain_text):
    
    plain_text = plain_text.lower()
    
    trans = str.maketrans(letters, e_letters, " ,.")
    result = list(plain_text.translate(trans))
    
    for i in range(1,len(result)):
        if i%5 == 0:
            result[i] = " " + result[i]
            
    return "".join(result)



def decode(ciphered_text):
    
    trans = str.maketrans(e_letters, letters, " ")
    result = ciphered_text.translate(trans)
    
    return result

