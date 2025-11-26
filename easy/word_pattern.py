# My solution

def word_pattern(pattern, s):
    p, c = 0, 0
    record = {}
    
    while p < len(pattern):
        if c > len(s) - 1:
            return False
        
        if s[c] == ' ':
            c += 1
            continue
        
        w = ''
        
        while c < len(s) and s[c] != ' ':
            w += s[c]
            c += 1
            
        if pattern[p] in record:
            if record[pattern[p]] != w:
                return False

        else:
            record[pattern[p]] = w
            
        p += 1
        
    if c < len(s) - 1:
        return False
    
    return True

print(word_pattern('abba', 'dog cat cat dog'), True)
print(word_pattern('abba', 'dog cat cat fish'), False)
print(word_pattern('abba', 'dog cat cat dog dog'), False)
print(word_pattern('abbaa', 'dog cat cat dog'), False)

# Neetcode's solution

class Solution:
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
