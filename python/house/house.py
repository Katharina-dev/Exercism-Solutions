largest_clause = ["This is the horse and the hound and the horn",
          "that belonged to the farmer sowing his corn",
          "that kept the rooster that crowed in the morn",
          "that woke the priest all shaven and shorn",
          "that married the man all tattered and torn",
          "that kissed the maiden all forlorn",
          "that milked the cow with the crumpled horn",
          "that tossed the dog",
          "that worried the cat",
          "that killed the rat",
          "that ate the malt",
          "that lay in the house that Jack built."]

def line(n):
    if n == 12:
        return largest_clause[-12]
    elif n in (1, 11):
        return "This is " + " ".join(largest_clause[-n].split(" ")[3:])
    else:
        return "This is " + " ".join(largest_clause[-n].split(" ")[2:])

def clause(n):
    if n == 1:
        return line(n)
    else:
        return line(n) + " " + " ".join(largest_clause[-n+1:])

def recite(start_verse, end_verse):
    result = []
    for i in range(start_verse, end_verse+1):
        result.append(clause(i))
    return result

