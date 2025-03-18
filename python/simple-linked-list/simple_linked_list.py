class Node:
    
    def __init__(self, data):
        self.data = data
        self.foll = None

    def value(self):
        return self.data

    def next(self):
        return self.foll


class LinkedList:
    
    def __init__(self, values=[]):
        values = list(values)
        self.values = []
        if values:
            node = Node(data=values.pop(0))
            self.values.append(node)
            for elem in values:
                new_node = Node(data=elem)
                new_node.foll = node
                node = new_node
                self.values.append(node)
            self.last_node = node

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        self.values.reverse()
        return iter([i.data for i in self.values])
        
    def head(self):
        if not self.values:
            raise EmptyListException("The list is empty.")
        return self.last_node

    def push(self, value):
        if not self.values:
            self.last_node = Node(data=value)
        else:
            new_node = Node(data=value)
            new_node.foll = self.last_node
            self.last_node = new_node
        self.values.append(self.last_node)

    def pop(self):
        if not self.values:
            raise EmptyListException("The list is empty.")
        else:
            node = self.values.pop()
            if self.values:
                self.last_node = self.values[-1]
        return node.data

    def reversed(self):
        return [item.data for item in self.values]

class EmptyListException(Exception):
    
    def __init__(self, message):
        self.message = message
