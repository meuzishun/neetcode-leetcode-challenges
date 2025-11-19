# My solution

def valid_palindrome_II(s):
    l, r = 0, len(s) - 1
    mismatch_count = 0
    
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            mismatch_count += 1
            
            if mismatch_count > 1:
                return False
            
            if s[l + 1] == s[r]:
                l += 1
            else:
                r -= 1
    
    return True

print('PASS' if valid_palindrome_II('aba') == True else 'FAIL')
print('PASS' if valid_palindrome_II('abca') == True else 'FAIL')
print('PASS' if valid_palindrome_II('abc') == False else 'FAIL')
print('PASS' if valid_palindrome_II('abcdca') == True else 'FAIL')

# NeetCode's solution

class Solution:
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return (skipL == skipR[::-1] or skipR == skipL[::-1])
            l, r = l + 1, r + 1
        return True
