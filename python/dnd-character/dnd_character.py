import random

class Character:
    
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        return random.randint(3,18)

    
def modifier(score):
    return (score-10)//2


