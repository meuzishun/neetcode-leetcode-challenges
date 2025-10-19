# My solution

class Solution:
    def min_cost(self, cost: list) -> int:
        res = 0
        
        i = len(cost) - 1
        
        while i > -1:
            curr = cost[i]
            next = cost[i - 1] if i - 1 > -1 else 0
            
            if curr < next:
                res += curr
                i -= 1
            else:
                res += next
                i -= 2
        
        return res

cost1 = [10, 15, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

solution = Solution()

print(solution.min_cost(cost1))
print(solution.min_cost(cost2))

# Neetcode's solution

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])