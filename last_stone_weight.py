# My solution

def last_store_weight(array):
    while len(array) > 1:
        max1 = max(array)
        array.remove(max1)
        
        max2 = max(array)
        array.remove(max2)
        
        diff = max1 - max2
        
        if diff > 0:
            array.append(diff)
        
    return array[0] if array else 0

print(last_store_weight([2, 7, 4, 1, 8, 1]))

# Neetcode's solution

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
                
        stones.append(0)
        return abs(stones[0])