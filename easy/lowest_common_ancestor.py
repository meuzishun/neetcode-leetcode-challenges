# My attempt

def lowest_common_ancestor(tree, p, q):
    node = tree
    
    while node:
        if (p < node.value and q > node.value) or (p == node.value or q == node.value):
            return node.value
        
        if p < node.value and q < node.value:
            node = node.left
            
        if p > node.value and q > node.value:
            node = node.right

# Neetcode's solution

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
