# My attempt

def num_bits(num):
    res = 0
    
    for i in range(1, 32):
        exp = 2**(i)
        print(exp, num // exp, num % exp)
        
        # if num > exp and num // exp < 2 and num % exp != 0:
        #     res += 1
        
        
    
    return res

print(num_bits(11))

# Neetcode's solution

class Solution:
    def hammingWeight(self, n):
        res = 0
        
        # Shifting bits
        # while n:
        #     res += n % 2
        #     n = n >> 1
        # return n
        
        # AND operation with bits
        while n:
            n &= (n - 1)
            res += 1
        return n