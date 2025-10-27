# My solution

def can_place_flowers(flowerbed, n):
    total, local = 0, 1
    
    for i, v in enumerate(flowerbed):
        if v == 1:
            if local > 2:
                total += abs((local - 1) // 2)
            local = 0
        else:
            local += 1
        
    if local > 1:
        total += local // 2
    
    return n <= total

print(can_place_flowers([1, 0, 0, 0, 1], 1))
print(can_place_flowers([1, 0, 0, 0, 1], 2))
print(can_place_flowers([0, 0, 1], 1))
print(can_place_flowers([1, 0, 0], 1))

# Neetcode's solution

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # f = [0] + flowerbed + [0]
        
        # for i in range(1, len(f) - 1):
        #     if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
        #         f[i] = 1
        #         n -= 1
        # return n <= 0
        
        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1
                
        n -= (empty) // 2
        return n <= 0