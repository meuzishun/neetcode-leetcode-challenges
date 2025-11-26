# My solution

def majority_element(nums):
    majority = len(nums) / 2
    counts = {}
    
    for val in nums:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
        
        if counts[val] > majority:
            return val

print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))

# Neetcode's solution

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # count= {}
        # res, maxCount = 0, 0
        
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n], maxCount)
        # return res
        
        res, count = 0, 0
        
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res