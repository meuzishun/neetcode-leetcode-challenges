# My solution

def find_pivot_index(nums):
    left_sum, right_sum = 0, 0
    
    for n in nums:
        right_sum += n
    
    for i, n in enumerate(nums):
        right_sum -= n
        
        if left_sum == right_sum:
            return i
        
        left_sum += n
    
    return -1

print(find_pivot_index([1, 7, 3, 6, 5, 6]))
print(find_pivot_index([100, 73, 3, 99, 20, 54]))
print(find_pivot_index([1, 2, 3, 4, 5, 6]))

# Neetcode's solution

class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
