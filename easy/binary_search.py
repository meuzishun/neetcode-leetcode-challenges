# My solution

def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = r + l // 2 # ! Oops... check order of operations here
        
        if nums[m] == target:
            return m
        
        if nums[m] < target:
            l = m + 1
            continue

        if nums[m] > target:
            r = m - 1
            continue
    
    return -1

print(binary_search([-1, 0, 3, 5, 9, 12], 9), 4)
print(binary_search([-1, 0, 3, 5, 9, 12], 2), -1)

# Neetcode's solution

class Solution:
    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # m = (l + r) // 2
            m = l + ((r - l) // 2) # Avoid overflow with very large arrays
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1