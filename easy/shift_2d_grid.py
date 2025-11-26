# My solution

def shift_2d_grid(grid, k):
    arr = []
    n = len(grid[0])
    
    for row in grid:
        for val in row:
            arr.append(val)
    
    shifted = arr[k:] + arr[:k]
    
    res = []
    
    for [i, v] in enumerate(shifted):
        if i % n == 0:
            row = []
            row.append(v)
            res.append(row)
        else:
            res[-1].append(v)
    
    return res
    
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(shift_2d_grid(grid, 1))

# Neetcode's solution

class Solution:
    def shiftGrid(self, grid, k):
        M, N = len(grid), len(grid[0])
        
        def posToVal(r, c):
            return r * N + c
        def valToPos(v):
            return [v // N, v % N]
        
        res = [[0] * N for i in range(M)]
        for r in range(M):
            for c in range(N):
                newVal = (posToVal(r, c) + k) % (M * N)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
        return res