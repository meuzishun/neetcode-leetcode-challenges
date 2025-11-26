# My solution

def move_zeros(nums):
    l, r = 0, 1
    
    while r < len(nums):
        if nums[r] != 0 and nums[l] == 0:
            nums[l], nums[r] = nums[r], 0
        
        if nums[l] != 0:
            l += 1
        
        r += 1
    
    return nums

print(move_zeros([0, 1, 0, 3, 12]))

# Neetcode's solution

class Solution:
    def moveZeros(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums