# My solution

def find_missing(nums):
    count = set()
    
    for i in range(1, len(nums) + 1):
        count.add(i)

    for n in nums:
        if n in count:
            count.remove(n)
        
    return list(count)


print(find_missing([1, 2, 3, 4, 3]), [5])
print(find_missing([2, 2, 3, 3, 3]), [1, 4, 5])

# Neetcode's solution

class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res