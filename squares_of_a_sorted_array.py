# My solution

def squares_of_a_sorted_array(nums):
    res = []
    mid = 0
    l, r = 0, 0
    for i, n in enumerate(nums):
        if n > mid:
            break
        if abs(n) <= mid:
            mid = n
            l = i - 1
            r = i + 1
    res.append(mid)
    while l > -1 or r < len(nums):
        if nums[l]**2 < nums[r]**2:
            res.append(nums[l]**2)
            l -= 1
        else:
            res.append(nums[r]**2)
            r += 1
    return res
    # negSqrs = []
    # posSqrs = []
    # res = []
    
    # for n in nums:
    #     if n < 0:
    #         negSqrs.append(n**2)
    #     else:
    #         posSqrs.append(n**2)
    
    # np, pp = len(negSqrs) - 1, 0 

    # while np > -1 or pp < len(posSqrs):
    #     if pp > len(posSqrs) or negSqrs[np] < posSqrs[pp]:
    #         res.append(negSqrs[np])
    #         np -= 1
    #     if np < 0 or posSqrs[pp] < negSqrs[np]:
    #         res.append(posSqrs[pp])
    #         pp += 1

    # return res

print(squares_of_a_sorted_array([-4, -1, 0, 3, 10]))

# Neetcode's solution

class Solution:
    def sortedSquares(self, nums):
        res = []
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r += 1
        
        return res[::-1]

# GPT:
def solution(nums):
    res = [0] * len(nums)
    l, r = 0, len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[l]) > abs(nums[r]):
            res[i] = nums[l] * nums[l]
            l += 1
        else:
            res[i] = nums[r] * nums[r]
            r -= 1
    return res