def tree_from_traversals(preorder, inorder):
    
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    
    elif set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    
    elif len(preorder) != len(set(preorder)) or len(inorder) != len(set(inorder)
                                                                    ):
        raise ValueError("traversals must contain unique items")
    
    return tree(preorder, inorder)

        
def tree(preorder, inorder):
    
    if preorder == []:
        return {}
    
    root_index = inorder.index(preorder[0])
    
    return {"v": preorder[0],
            "l": tree(preorder[1:root_index+1], inorder[:root_index]),
            "r": tree(preorder[root_index+1:], inorder[root_index+1:])} 
