# My solution

def remove_duplicates(array):
    dup_count = 0
    
    for i, curr in enumerate(array):
        if array[i + 1] == '_':
            break
        
        while curr == array[i + 1]:
            array.pop(i + 1)
            array.append('_')
            dup_count += 1
    
    return [dup_count, array]

print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# Neetcode's solution

class Solution:
    def removeDuplicates(self, nums):
        l = 1
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
                
        return l
