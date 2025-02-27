def convert(number):
    
    Pling = "Pling" if number%3 == 0 else ""
    Plang = "Plang" if number%5 == 0 else ""
    Plong = "Plong" if number%7 == 0 else ""
    sounds = Pling + Plang + Plong
    
    return sounds if sounds else str(number)
    
