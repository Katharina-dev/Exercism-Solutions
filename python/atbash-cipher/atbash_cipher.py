def encode(plain_text):
    text_array = [i for i in plain_text if i.isalnum()]
    text_cipher = [chr(26 - (ord(i.lower()) - 96) + 97) if i.isalpha() else i for i in text_array]
    parts = len(text_cipher)//5
    return ' '.join([''.join(text_cipher[i*5:i*5+5]) for i in range(parts) if parts>0]  + [''.join(text_cipher[parts*5:])]).strip()


def decode(ciphered_text):
    text_array = [i for i in (ciphered_text.replace(' ', '')) if i.isalnum()]
    text_cipher = [chr(26 - (ord(i) - 96) + 97) if i.isalpha() else i for i in text_array]
    return ''.join(text_cipher)

