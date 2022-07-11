# Globals for the directions

EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)
    
    def move(self, movement):
        for m in movement:
            if m == "R":
                self.direction = (self.direction + 1)%4
            elif m == "L":
                self.direction = (self.direction - 1)%4
            elif m == "A":
                if self.direction == 0:
                    self.y_pos += 1
                elif self.direction == 1:
                    self.x_pos += 1
                elif self.direction == 2:
                    self.y_pos -= 1
                elif self.direction == 3:
                    self.x_pos -= 1


