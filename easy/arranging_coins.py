# My solution (algebra)

def arranging_coins(n):
    return int((-1 + ((1 + 8 * n) ** 0.5)) // 2)

print(arranging_coins(21))
print(arranging_coins(19))
print(arranging_coins(5))

# Neetcode's solution (binary search)

class Solution:
    def arrangeCoins(self, n):
        l, r = 1, n
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res
