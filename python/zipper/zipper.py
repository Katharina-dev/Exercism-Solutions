class Node:
    
    def __init__(self, value, left=None, right=None):
        
        self.value = value
        self.left = left
        self.right = right
        
    def node_to_tree(self):
        
        if self.left is None and self.right is None:
            return {"value": self.value, "left": None, "right": None}
        elif self.left is None:
            return {"value": self.value, "left": None, "right": self.right.node_to_tree()}
        elif self.right is None:
            return {"value": self.value, "left": self.left.node_to_tree(), "right": None}
        else:
            return {"value": self.value, "left": self.left.node_to_tree(), "right": self.right.node_to_tree()}
 
class Zipper:
    
    def __init__(self, tree):
        
        self.focus = self.root = Zipper.create_tree(tree)
        self.visited = []
        
    @staticmethod
    def create_tree(tree):
        
        if tree['left'] is None and tree['right'] is None:
            return Node(tree['value'])
        elif tree['left'] is None:
            return Node(tree['value'], None, Zipper.create_tree(tree['right']))
        elif tree['right'] is None:
            return Node(tree['value'], Zipper.create_tree(tree['left']), None)
        else:
            return Node(tree['value'], Zipper.create_tree(tree['left']), Zipper.create_tree(tree['right']))
    
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)
    
    def value(self):
        return self.focus.value
    
    def set_value(self, value):
        
        self.focus.value = value
        return self
    
    def left(self):
        
        self.visited.append(self.focus)
        self.focus = self.focus.left
        return self if self.focus else None
    
    def set_left(self, subtree):
        
        self.focus.left = Zipper.create_tree(subtree) if subtree else None
        return self
    
    def right(self):
        
        self.visited.append(self.focus)
        self.focus = self.focus.right
        return self if self.focus else None
    
    def set_right(self, subtree):
        
        self.focus.right = Zipper.create_tree(subtree) if subtree else None
        return self
    
    def up(self):
        
        self.focus = self.visited.pop() if self.visited else None
        return self if self.focus else None
        
    def to_tree(self):
        return self.root.node_to_tree() 
    
