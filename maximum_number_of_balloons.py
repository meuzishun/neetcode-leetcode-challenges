# My solution

def maxBalloons(text):
    numOfBalloons = len(text) // 8
    counts = {}
    
    for c in text:
        if c in 'balloon':
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

    for k, v in counts.items():
        if k == 'l' or k == 'o':
            v = v // 2
        numOfBalloons = min(numOfBalloons, v)
    
    return numOfBalloons

print(maxBalloons('nlaebolko'), 1)
print(maxBalloons('loonbalxballpoon'), 2)

# Neetcode's solution

class Solution:
    def maxNumberOfBalloons(self, text):
        countText = Counter(text)
        balloon = Counter('balloon')
        
        res = len(text)
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res
