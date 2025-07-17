import random
from string import ascii_lowercase as letters
from itertools import cycle

class Cipher:
    
    def __init__(self, key=None):
        self.key = key if key else "".join(random.choice(letters) for _ in range(100))
        
    def encode(self, text):
        encoded = []
        for l1, l2 in zip(text, cycle(self.key)):
            encoded.append(letters[(ord(l1) % 97 + ord(l2) % 97) % 26])
        return "".join(encoded)
        
    def decode(self, text):
        decoded = []
        for l1, l2 in zip(text, cycle(self.key)):
            decoded.append(letters[(ord(l1) % 97 - ord(l2) % 97) % 26])
        return "".join(decoded) 

