class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    
class WordSearch:
    
    def __init__(self, puzzle):
        self.puzzle = puzzle
        
    def search(self, word):
        
        if len(self.puzzle[0]) == 1:
            return None
        
        #moving row
        for number, line in enumerate(self.puzzle):
            #forward
            if word in line:
                ind = line.find(word)
                return (Point(ind, number), Point(ind+len(word)-1, number))
            #back
            elif word in line[::-1]:
                ind = line[::-1].find(word)
                return (Point(len(line)-ind-1, number), Point(len(line)-ind-len(word), number))

        #moving column                
        for number in range(len(self.puzzle)):
            line = ''.join([letters[number] for letters in self.puzzle])
            #forward
            if word in line:
                ind = line.find(word)
                return (Point(number, ind), Point(number, ind+len(word)-1))
            #back
            elif word in line[::-1]:
                ind = line[::-1].find(word)
                return (Point(number, len(line)-ind-1), Point(number, len(line)-ind-len(word)))
        
        #moving diagonal
        for number in range(len(self.puzzle)):
            #from the left side
            #up
            line1 = ''.join([self.puzzle[number-n][n] for n in range(number+1)])
            if word in line1:
                ind = line1.find(word)
                return (Point(ind, number-ind), Point(ind+len(word)-1, number-ind-len(word)+1))
            #down
            line2 = ''.join([self.puzzle[n][n-number] for n in range(number, len(self.puzzle))])
            if word in line2:
                ind = line2.find(word)
                return (Point(number+ind, ind), Point(number+ind+len(word)-1, ind+len(word)-1))
            elif word in line2[::-1]:
                ind = line2[::-1].find(word)
                return (Point(len(line2)-ind-1, number+len(line2)-ind-1), Point(len(line2)-ind-len(word), number+len(line2)-ind-len(word)))
            #from the right side
            #up
            line3 = ''.join([self.puzzle[number-n][len(self.puzzle)-1-n] for n in range(number+1)])
            if word in line3:
                ind = line3.find(word)
                return (Point(number+ind, ind), Point(number+ind+len(word)-1, ind+len(word)-1))
            #down
            line4 = ''.join([self.puzzle[n][len(self.puzzle)+number-1-n] for n in range(number, len(self.puzzle))])
            if word in line4:
                ind = line4.find(word)
                return (Point(len(self.puzzle)-1-ind, number+ind), Point(len(self.puzzle)-ind-len(word), number+ind+len(word)-1))
                        

