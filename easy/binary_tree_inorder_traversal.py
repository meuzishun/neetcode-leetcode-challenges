# Neetcode's solution

class Solution:
    def inorderTraversal(self, root):
        # * Iterative
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        # * Recursive 
        # res = []
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)

        # inorder(root)
        # return res

