WHITE = 'W'
BLACK = 'B'
NONE = ' '

class Board:
    
    """Count territories of each player in a Go game
 
    Args:
        board (list[str]): A two-dimensional Go board
    """
    
    def __init__(self, board):
        self.board = board
        self.owners = {"W": set(),
                       "B": set(),
                       " ": set()}
        
    def visited(self, row, col):
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]) or self.board[row][col] == " " and (col, row) in self.visited_cells:
            return
        elif self.board[row][col] == "B" or self.board[row][col] == "W":
            self.visited_letters.append(self.board[row][col])
        else:
            self.visited_cells.append((col, row))
            self.visited(row-1, col)
            self.visited(row+1, col)
            self.visited(row, col-1)
            self.visited(row, col+1)
            
    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board
 
        Args:
            x (int): Column on the board
            y (int): Row on the board
 
        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if x < 0 or x >= len(self.board[0]) or y < 0 or y >= len(self.board):
            raise ValueError('Invalid coordinate')
        self.visited_cells = []
        self.visited_letters = []
        self.visited(y, x)
        letter = " " if not self.visited_cells or len(set(self.visited_letters)) != 1 else self.visited_letters[0]
        return (letter, set(self.visited_cells))
    
    def territories(self):
        """Find the owners and the territories of the whole board
 
        Args:
            none
 
        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                letter, visited_cells = self.territory(column, row)
                self.owners[letter] = self.owners[letter].union(visited_cells)
        return self.owners
    
