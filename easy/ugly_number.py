# My solution

def is_ugly_number(num):
    primes = [2, 3, 5]
    
    for prime in primes:
        if num in primes:
            return True
        
        while num % prime == 0 and num not in primes:
            num = num / prime
        
    return False

print(is_ugly_number(6))
print(is_ugly_number(8))
print(is_ugly_number(20))
print(is_ugly_number(21))

# Neetcode's solution

class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p
            
        return n == 1