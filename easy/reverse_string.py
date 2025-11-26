# My solution

def reverse_string(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        tmp = s[l]
        s[l] = s[r]
        s[r] = tmp
        l += 1
        r -= 1
    
    return s


string1 = ['h', 'e', 'l', 'l', 'o']
print(reverse_string(string1), ['o', 'l', 'l', 'e', 'h'])
print(string1, ['o', 'l', 'l', 'e', 'h'])

string2 = ['H', 'a', 'n', 'n', 'a', 'h']
print(reverse_string(string2), ['h', 'a', 'n', 'n', 'a', 'H'])
print(string2, ['h', 'a', 'n', 'n', 'a', 'H'])

# Neetcode's solution

class Solution:
    def reverseString(self, s):
        # Time: O(n) Space: O(1) - Actual answer
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
            
        # Time: O(n) Space: O(n) - Stack
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
        
        # Time: O(n) Space: O(n) - Recursion
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
        reverse(0, len(s) - 1)
