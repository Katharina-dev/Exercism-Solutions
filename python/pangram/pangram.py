def is_pangram(sentence):
    
    sentence = sentence.lower()
    presence = [sentence.find(chr(i)) for i in range(97,123)]
    for letter in presence:
        if letter < 0:
            return False
    return True
