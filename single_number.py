# My solution (does NOT use constant extra space)

def single_number(nums):
    single = set()
    
    for n in nums:
        if n not in single:
            single.add(n)
        else:
            single.remove(n)
        
    return single.pop()

print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))

# Neetcode's solution (bit manipulation, XOR (^))

class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = n ^ res
        res