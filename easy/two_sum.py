# My solution

def two_sum(nums, target):
    diff_hist = []
    
    for i in range(len(nums)):
        if nums[i] in diff_hist:
            return [diff_hist.index(nums[i]), i]
        
        diff_hist.append(target - nums[i])
        

print(two_sum([2,7,11,15], 26))

# NeetCode solution

class Solution:
    # ! Not using typing like video
    def twoSum(self, nums, target):
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i
        
        return

test = Solution()
print(test.twoSum([2,7,11,15], 26))