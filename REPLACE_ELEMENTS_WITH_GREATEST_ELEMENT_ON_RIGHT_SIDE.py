# My solution

def REPLACE_ELEMENTS_WITH_GREATEST_ELEMENT_ON_RIGHT_SIDE(arr):
    result = [-1]
    
    for i in range(len(arr) - 2, -1, -1):
        result.insert(0, max(result[0], arr[i + 1]))
        
    return result

print(REPLACE_ELEMENTS_WITH_GREATEST_ELEMENT_ON_RIGHT_SIDE([17, 18, 5, 4, 6, 1]))

# Neetcode's solution

class Solution:
    def replaceElements(self, arr):
        # initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])
        
        rightMax = -1
        
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        
        return arr
