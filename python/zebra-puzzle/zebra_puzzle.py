class House:
    
    def __init__(self, color, nationality, drink, smoke, pet):
        self.color = color
        self.nationality = nationality
        self.drink = drink
        self.smoke = smoke
        self.pet = pet

        
houses = [House('yellow', 'Norwegian', 'water', 'Kool', 'fox'),
         House('blue', 'Ukrainian', 'tea', 'Chesterfield', 'horse'),
         House('red', 'Englishman', 'milk', 'Old Gold', 'snails'),
         House('ivory', 'Spaniard', 'orange juice', 'Lucky Strike', 'dog'),
         House('green', 'Japanese', 'coffee', 'Parliament', 'zebra')]


def drinks_water():
    for house in houses:
        if house.drink == 'water':
            return house.nationality

        
def owns_zebra():
    for house in houses:
        if house.pet == 'zebra':
            return house.nationality
