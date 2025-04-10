from math import gcd

class Rational:
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.reduce().standard()
        
    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom
    
    def __repr__(self):
        return f'{int(self.numer)}/{int(self.denom)}'
    
    def __add__(self, other):
        self.numer = self.numer * other.denom + other.numer * self.denom
        self.denom = self.denom * other.denom
        return self.reduce().standard()
    
    def __sub__(self, other):
        self.numer = self.numer * other.denom - other.numer * self.denom
        self.denom = self.denom * other.denom
        return self.reduce().standard()
    
    def __mul__(self, other):
        self.numer *= other.numer
        self.denom*= other.denom
        return self.reduce().standard()
    
    def __truediv__(self, other):
        self.numer *= other.denom
        self.denom = other.numer * self.denom
        return self.reduce().standard()
    
    def __abs__(self):
        self.numer = self.numer if self.numer >= 0 else -self.numer
        self.denom = self.denom if self.denom >= 0 else -self.denom
        return self.reduce()
    
    def __pow__(self, power):
        if power >= 0:
            self.numer **= power
            self.denom **= power
        else:
            self.numer_ = self.denom ** (-power)
            self.denom = self.numer ** (-power)
            self.numer = self.numer_
        return self.reduce().standard()
    
    def __rpow__(self, base):
        return pow(base, self.numer/self.denom)
    
    def reduce(self):
        self.gcd = gcd(self.numer, self.denom)
        self.numer = int(self.numer / self.gcd)
        self.denom = int(self.denom / self.gcd)
        return self
    
    def standard(self):
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1
        return self
