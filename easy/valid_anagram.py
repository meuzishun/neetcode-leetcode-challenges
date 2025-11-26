from collections import Counter

def valid_anagram(s, t):
    if len(s) != len(t):
        return False
# My solution
    
    s_dict = {}
    
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
    
    t_dict = {}
    
    for c in t:
        if c in t_dict:
            t_dict[c] += 1
        else:
            t_dict[c] = 1
            
    for k, v in s_dict.items():
        if k not in t_dict:
            return False
        if t_dict[k] != v:
            return False
    
    return True

print(valid_anagram('asdf', 'fdsa'))
print(valid_anagram('qwerpoiu', 'rewquiop'))
print(valid_anagram('asdf;lkj', 'rewquiop'))
print(valid_anagram('aas', 'sas'))
print(valid_anagram('aassddff', 'ffddssaa'))

# NeetCode solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # * If we care about space rather than time complexity:
        # return sorted(s) == sorted(t)
        
        # ! Kinda cheating...:
        # return Counter(s) == Counter(t)
        
        # * Probably the preferred solution:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True