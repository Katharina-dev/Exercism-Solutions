from json import dumps

class Tree:
    
    def __init__(self, label, children=None):
        
        self.label = label
        self.children = children if children is not None else []
        
    def find(self, name, visited):
        
        if self.label == name:
            new_node = Tree(self.label, self.children)
            visited.append(new_node)
            return new_node
        
        elif self.children:
            for child in self.children:
                new_node = Tree(self.label, [ch for ch in self.children if ch != child])
                root = child.find(name, visited)
                if root:
                    root.children.append(new_node)
                    visited.append(new_node)
                    return new_node
                
    def __dict__(self):
        
        return {self.label: [c.__dict__() for c in sorted(self.children)]}
    
    def __str__(self, indent=None):
        
        return dumps(self.__dict__(), indent=indent)
    
    def __lt__(self, other):
        
        return self.label < other.label
    
    def __eq__(self, other):
        
        return self.__dict__() == other.__dict__()
    
    def from_pov(self, from_node):
        
        visited = []
        self.find(from_node, visited)
        if not visited:
            raise ValueError("Tree could not be reoriented")
        return visited[0]
    
    def path_to(self, from_node, to_node):
        
        visited1 = []
        self.find(from_node, visited1)
        if not visited1:
            raise ValueError("Tree could not be reoriented")
        visited2 = []
        visited1[0].find(to_node, visited2)
        if not visited2:
            raise ValueError("No path found")
        return [vis.label for vis in reversed(visited2)]
    
