# My solution

def next_greater_element(nums1, nums2):
    # * brute force
    # ans = []
    # for n in nums1:
    #     found = False
    #     max = -1
    #     for m in nums2:
    #         if m == n:
    #             found = True
    #             continue
            
    #         if found and m > n and m > max:
    #             max = m
    #             break
    #     ans.append(max)
    # return ans
    
    # * with stack
    hist = []
    lookup = {}
    
    for i in range(len(nums2) - 1, -1, -1):
        while len(hist) > 0 and hist[-1] < nums2[i]:
            hist.pop()
            
        if len(hist) == 0:
            lookup[nums2[i]] = -1
        else:
            lookup[nums2[i]] = hist[-1]
        
        hist.append(nums2[i])
        
    ans = []
    for n in nums1:
        ans.append(lookup[n])
        
    return ans
    
print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_element([4, 1, 2], [2, 1, 3, 4]))

# Neetcode's solution

class Solution:
    
    def nextGreaterElement(self, nums1, nums2):
        # * stack
        nums1Idx = { n: i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)
        
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
        
        # * Brute force
        # nums1Idx = { n: i for i, n in enumerate(nums1) }
        # res = [-1] * len(nums1)
        
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1Idx:
        #         continue
        #     for j in range(i + 1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = nums1Idx[nums2[i]]
        #             res[idx] = nums2[j]
        #             break
        # return res
    
    # 