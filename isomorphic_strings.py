# My solution

def are_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    lookup = {}
    
    for i in range(len(s)):
        if s[i].lower() not in lookup:
            lookup[s[i].lower()] = t[i].lower()
        
        if t[i].lower() not in lookup:
            lookup[t[i].lower()] = s[i].lower()
            
        if lookup[s[i].lower()] != t[i].lower() or lookup[t[i].lower()] != s[i].lower():
            return False
        
    return True

print(are_isomorphic('add', 'egg'))
print(are_isomorphic('foo', 'bar'))
print(are_isomorphic('bar', 'foo'))

# Neetcode's solution

class Solution:
    def isIsomorphic(self, s, t):
        mapST, mapTS = {}, {}
        
        for c1, c2 in zip(s, t):

            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            
            mapST[c1] = [c2]
            mapTS[c2] = [c1]
        
        return True