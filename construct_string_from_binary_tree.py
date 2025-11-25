# My solution

def construct_string_from_binary_tree(node):
    if not node:
        return ''

    res = str(node['val'])
    subL = construct_string_from_binary_tree(node['left'])
    subR = construct_string_from_binary_tree(node['right'])
    
    if subL:
        res += f'({subL})'
    if subR:
        res += f'({subR})'
        
    return res
        
tree = {
    'val': 1,
    'left': {
        'val': 2,
        'left': {
            'val': 4,
            'left': None,
            'right': None
        },
        'right': None,
    },
    'right': {
        'val': 3,
        'left': None,
        'right': None,
    }
}

print(construct_string_from_binary_tree(tree))

# Neetcode's solution

class Solution:
    def tree2str(self, root):
        res = []
        
        def preorder(root):
            if not root:
                return
            
            res.append('(')
            res.append(str(root.val))
            
            if not root.left and root.right:
                res.append('()')
            preorder(root.left)
            preorder(root.right)
            res.append(')')
        
        preorder(root)
        return ''.join(res)[1:-1]