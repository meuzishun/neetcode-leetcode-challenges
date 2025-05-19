class Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
test = Solution()

test.rob([1, 2, 3, 1])
test.rob([3, 5, 1, 6, 8, 3, 1, 5, 9])