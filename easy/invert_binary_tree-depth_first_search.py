# My ATTEMPT

def invert_binary_tree(root):
    if not root.left and not root.right:
        return
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    
    return root

# Neetcode's solution

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root