# My solution

def baseball_game(ops):
    stack = []
    
    for i in ops:
        if i == '+':
            stack.append(stack[-1] + stack[-2])
            continue
        
        if i == 'D':
            stack.append(stack[-1] * 2)
            continue
        
        if i == 'C':
            stack.pop()
            continue
        
        stack.append(int(i))
        
    res = 0
    
    for i in stack:
        res += i
        
    return res

print(baseball_game(['5', '2', 'C', 'D', '+']) == 30)

# Neetcode's solution

class Solution:
    def calPoints(self, ops):
        stack = []
        
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)