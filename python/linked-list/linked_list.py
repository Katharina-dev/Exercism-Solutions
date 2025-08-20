class Node:
    
    def __init__(self, value, prev=None, foll=None):
        self.value = value
        self.prev = prev
        self.foll = foll
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __len__(self):
        return self.length
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.foll
            
    def push(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.foll = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        
        popped_value = self.tail.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.foll = None
            
        self.length -= 1
        return popped_value
        
    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        
        shifted_value = self.head.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.foll
            self.head.prev = None
            
        self.length -= 1
        return shifted_value
        
    def unshift(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.foll = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1
        
    def delete(self, value):
        if self.length == 0:
            raise ValueError("Value not found")
        current_node = self.head
       
        while current_node:
            if current_node.value == value:
                if current_node.prev:
                    current_node.prev.foll = current_node.foll
                else:
                    self.head = current_node.foll
                
                if current_node.foll:
                    current_node.foll.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                
                self.length -= 1
                return 
            current_node = current_node.foll
        
        raise ValueError("Value not found")
