# My solution

class GuessGame:
    def __init__(self, pick):
        self.pick = pick
        
    def guess(self, num):
        if num > self.pick:
            return -1
        if num < self.pick:
            return 1
        if num == self.pick:
            return 0

game = GuessGame(6)

def findPick(n):
    low = 0
    high = n
    
    while True:
        mid = ((high - low) // 2) + low
        res = game.guess(mid)
        if res == -1:
            high = mid
        if res == 1:
            low = mid
        if res == 0:
            return mid

print(findPick(10))

# Neetcode's solution

class Solution:
    def guessNumber(self, n):
        l, r = 1, n
        
        while True:
            m = (l + r) // 2
            res = guess(m)
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m
