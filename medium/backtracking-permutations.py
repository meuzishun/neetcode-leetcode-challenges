# Neetcode's solution 1

class Solution:
    def permute(self, nums):
        result = []
        
        # base case
        if (len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
            
        return result

# Neetcode's solution 2

class Solution2:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res

# Neetcode's solution 3 (no recursion)

class Solution3:
    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
    
solution = Solution3()
print(solution.permute([1, 2, 3]))