from typing import List

# Going forwards:
nums = [0, 1, 2, 2, 3, 0, 4, 2]
nums = [0, 1, 3, 2, '_', 0, 4, 2]
nums = [0, 1, 3, 0, '_', '_', 4, 2]
nums = [0, 1, 3, 0, 4, '_', '_', 2]
nums = [0, 1, 3, 0, 4, '_', '_', '_']

# Going backwards?...
nums = [0, 1, 2, 2, 3, 0, 4, 2], (-1, -1) # HIT
nums = [0, 1, 2, 2, 3, 0, 4, '_'], (-2, -2)
nums = [0, 1, 2, 2, 3, 0, 4, '_'], (-3, -2)
nums = [0, 1, 2, 2, 3, 0, 4, '_'], (-4, -2)
nums = [0, 1, 2, 2, 3, 0, 4, '_'], (-5, -2) # HIT
nums = [0, 1, 2, 4, 3, 0, '_', '_'], (-6, -3) # HIT
nums = [0, 1, 0, 4, 3, '_', '_', '_'], (-7, -4) # HIT
nums = [0, 1, 0, 4, 3, '_', '_', '_'], (-8, -4)
# DONE

# My attempt (trying to predict Neetcode's syntax)

class Solution:
    # This works but not getting exactly the same output
    def removeElement(self, nums: List, val: int) -> int:
        # l, r, total = len(nums) - 1, len(nums) - 1, len(nums)

        # while l > -1:
        #     if nums[l] == val:
        #         nums[l] = nums[r]
        #         nums[r] = '_'
        #         total -= 1
        #         r -= 1
        #     l -= 1
        
        # return total
        
        l, r, total = 0, len(nums) - 1, len(nums)
        
        while l <= r:
            while nums[r] == val:
                nums[r] = '_'
                total -= 1
                r -= 1
            if nums[l] == val:
                nums[l] = nums[r]
                nums[r] = '_'
                total -= 1
                r -= 1
            l += 1
        
        return total
    
solution: Solution = Solution()

print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

# Neetcode's solution

class Solution:
    def removeElement(self, nums: List, val: int) -> int:
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k