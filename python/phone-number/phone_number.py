import re

class PhoneNumber:
    
    def __init__(self, number):
        
        self.number = ''.join(re.findall(r'[0-9]', number))
        
        if len(self.number) == 11 and int(self.number[0]) == 1:
            self.number = self.number[1:]
            
        if ''.join(re.findall(r'[a-z]', number)):
            raise ValueError("letters not permitted")
            
        if ''.join(re.findall(r'[&@]', number)):
            raise ValueError("punctuations not permitted")
            
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
            
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
            
        if len(self.number) == 11 and int(self.number[0]) != 1:
            raise ValueError("11 digits must start with 1")
            
        if int(self.number[-7]) == 0:
            raise ValueError("exchange code cannot start with zero")
            
        if int(self.number[-7]) == 1:
            raise ValueError("exchange code cannot start with one")
            
        if int(self.number[-10]) == 0:
            raise ValueError("area code cannot start with zero")
            
        if int(self.number[-10]) == 1:
            raise ValueError("area code cannot start with one")
            
        self.area_code = self.number[:3]

    def pretty(self):
        
        self.number = f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'
        
        return self.number
       
        
