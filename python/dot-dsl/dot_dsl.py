NODE, EDGE, ATTR = range(3)


class Node:
    
    def __init__(self, name, attrs):
        
        self.name = name
        self.attrs = attrs
        
    def __eq__(self, other):
        
        return self.name == other.name and self.attrs == other.attrs

    
class Edge:
    
    def __init__(self, src, dst, attrs):
        
        self.src = src
        self.dst = dst
        self.attrs = attrs
        
    def __eq__(self, other):
        
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)
    
class Graph:
    
    def __init__(self, data=None):
        
        self.nodes = []
        self.edges = []
        self.attrs = {}
        
        if data:
            
            if type(data) != list:
                raise TypeError("Graph data malformed")
            
            elif len(data[0]) < 3:
                raise TypeError("Graph item incomplete")
            
            elif data[0][0] not in [0, 1, 2]:
                raise ValueError("Unknown item")
            
            elif data[0][0] == 0 and type(data[0][1]) != str:
                raise ValueError("Node is malformed")
            
            elif data[0][0] == 1 and type(data[0][1]) != str:
                raise ValueError("Edge is malformed")
            
            elif data[0][0] == 2 and type(data[0][2]) != str:
                raise ValueError("Attribute is malformed")
            
            for i in range(len(data)):
                
                if data[i][0] == 0:
                    self.nodes.append(Node(data[i][1], data[i][2]))
                    
                elif data[i][0] == 1:
                    self.edges.append(Edge(data[i][1], data[i][2], data[i][3]))
                    
                elif data[i][0] == 2:
                    self.attrs[data[i][1]] = data[i][2] 
