# My first solution

def length_of_last_word(text):
    words = text.strip().split(' ')
    return len(words[-1])

print(length_of_last_word("   fly me    to    the  moon   "))

# My second solution

def length_of_last_word2(text):
    result = 0
    
    for i in range(len(text) - 1, 0, -1):
        if text[i] == ' ' and result == 0:
            continue
        elif text[i] == ' ' and result > 0:
            return result
        else:
            result += 1
        
    return result

print(length_of_last_word2("   fly me    to    the  moon   "))

# Neetcode's solution

class Solution:
    def lengthOfLastWord(self, s):
        i, length = len(s) - 1, 0
        
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length