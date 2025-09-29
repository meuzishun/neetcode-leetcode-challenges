# My solution

def valid_parentheses(str):
    match = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    open = match.values()
    
    record = []
    
    for char in str:
        if char in open:
            record.append(char)
            continue
        
        if len(record) == 0:
            return False
        
        if match[char] != record[-1]:
            return False
        
        record.pop()
        
    
    if len(record) > 0:
        return False
    
    return True

print(valid_parentheses('()[]{}'))
print(valid_parentheses('()'))
print(valid_parentheses('({)'))

# Neetcode's solution

class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{' }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False
        