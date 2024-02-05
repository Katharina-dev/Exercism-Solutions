from collections import Counter

class CustomSet:
    
    def __init__(self, elements=[]):
        self.elements = []
        for elem in elements:
            self.add(elem)
            
    def isempty(self):
        return not self.elements
    
    def __contains__(self, element):
        return element in self.elements
    
    def issubset(self, other):
        subset = [elem for elem in self.elements if elem in other.elements]
        return self.elements == subset
    
    def isdisjoint(self, other):
        subset = [elem for elem in self.elements if elem not in other.elements]
        return self.elements == subset
    
    def __eq__(self, other):
        self.set_()
        other.set_()
        return sorted(self.elements) == sorted(other.elements)
    
    def add(self, element):
        self.elements.append(element)
        return self
    
    def intersection(self, other):
        return CustomSet([elem for elem in self.elements if elem in other.elements])
    
    def __sub__(self, other):
        return CustomSet([elem for elem in self.elements if elem not in other.elements])
    
    def __add__(self, other):
        subset = CustomSet(self.elements + other.elements)
        subset.set_()
        return subset
    
    def set_(self):
         self.elements = [elem for elem in Counter(self.elements) if Counter(self.elements)[elem] > 0]

