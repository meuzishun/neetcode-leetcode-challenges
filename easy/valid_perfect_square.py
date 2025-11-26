# My solution (brute force or cheating)

def is_perfect_square(num):
    # i = 1
    
    # while True:
    #     res = i ** 2
        
    #     if res == num:
    #         return True
        
    #     if res > num:
    #         return False
        
    #     i += 1
    
    sqrt = num ** 0.5
    
    return int(sqrt) == sqrt

print(is_perfect_square(16), True)
print(is_perfect_square(14), False)
print(is_perfect_square(36), True)
print(is_perfect_square(24), False)

# Neetcode's solution (binary search)

class Solution:
    def validPerfectSquare(self, num):
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False

s = Solution()

print(s.validPerfectSquare(1))