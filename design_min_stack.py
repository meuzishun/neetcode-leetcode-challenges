# My solution

class MinStack:
    stack = []
    minHist = []
    
    def push(self, val):
        self.stack.append(val)
        if len(self.minHist) == 0 or val < self.minHist[-1]:
            self.minHist.append(val)
        else:
            self.minHist.append(self.minHist[-1])

    def pop(self):
        self.stack.pop()
        self.minHist.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minHist[-1]

stack = MinStack()

stack.push(-2)
stack.push(0)
stack.push(-3)

print(stack.getMin())
print(stack.pop())
print(stack.top())
print(stack.getMin())

# Neetcode's solution

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.minStack[-1]