# My solution

def is_number_happy(n):
    history = []
    
    while n != 1:
        n = sum([ int(c) ** 2 for c in list(str(n)) ])
        
        if n in history:
            print(history)
            return False
        
        history.append(n)

    print(history)
    return True

print(is_number_happy(2))

# Neetcode's solution

class Solution:
    def isHappy(self, n):
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
            
        return False
    
    def sumOfSquares(self, n):
        output = 0
        
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        
        return output