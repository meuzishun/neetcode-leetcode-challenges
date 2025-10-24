# My solution - the easy way:

# def contains_duplicate(nums):
#     return len(nums) != len(set(nums))

# print(contains_duplicate([1, 2, 3, 4]))
# print(contains_duplicate([1, 2, 3, 4, 4]))

# My solution - not cheating:

def contains_duplicate(nums):
    counts = set()
    
    for n in nums:
        if n in counts:
            return True
        counts.add(n)

    return False

print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 2, 3, 4, 4]))

# Neetcode's solution

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False