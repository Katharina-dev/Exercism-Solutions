class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
    def push(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.previous = new_node
            new_node.succeeding = self.tail
        else:
            self.head = new_node
        self.tail = new_node
    def pop(self):
        self.del_node = self.tail
        if self.tail.succeeding:
            self.tail = self.tail.succeeding
            self.tail.previous = None
        else:
            self.head = None
            self.tail = None
        return self.del_node.value

    def shift(self):
        self.del_node = self.head
        if self.head.previous:
            self.head = self.head.previous
            self.head.previous = None
        else:
            self.head = None
            self.tail = None
        return self.del_node.value

    def unshift(self, value):
        new_node = Node(value)
        if self.head:
            self.head.succeeding = new_node
            new_node.previous = self.head
        else:
            self.tail = new_node
        self.head = new_node
