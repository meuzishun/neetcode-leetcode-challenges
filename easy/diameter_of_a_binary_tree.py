class Solution:
    def diameterOfBinaryTree(self, root):
        res = [0] # the max diameter
        
        def dfs(root): # will update the max diameter but return the height
            if not root:
                return -1 # nodes without children have height of 0
            left = dfs(root.left) # left height
            right = dfs(root.right) # right height
            res[0] = max(res[0], 2 + left + right) # add 2 to account for edges

            return 1 + max(left, right) # returns height
        
        dfs(root)
        return res