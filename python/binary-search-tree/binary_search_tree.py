class TreeNode:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

    
class BinarySearchTree:
    
    def __init__(self, tree_data):
        self.tree_data = tree_data
        self.head = TreeNode(self.tree_data[0])
        for number in self.tree_data[1:]:
            self.paste_node(self.head, number)
            
    def paste_node(self, node, number):
        if number <= node.data:
            if not node.left:
                node.left = TreeNode(number)
            else:
                self.paste_node(node.left, number)
        elif number > node.data:
            if not node.right:
                node.right = TreeNode(number)
            else:
                self.paste_node(node.right, number)
                
    def sorting(self, node):
        if node == None:
            return []
        elif node.left == None and node.right == None:
            return [node.data]
        else:
            return self.sorting(node.left) + [node.data] + self.sorting(node.right)
    
    def data(self):
        return self.head
    
    def sorted_data(self):
        return self.sorting(self.head)

