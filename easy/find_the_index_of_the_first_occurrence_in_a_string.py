#  My solution

def sub_str_index(string, sub_string):
    if sub_string == '':
        return 0
    
    i, j, start = 0, 0, -1
    
    while i < len(string) and j < len(sub_string):
        if string[i] == sub_string[j]:
            if start < 0:
                start = i
            j += 1
        else:
            j = 0
            start = -1
        i += 1
    
    return start

print(sub_str_index('hello', 'll'))
print(sub_str_index('aaaaa', 'baa'))
print(sub_str_index('aaaaa', ''))
print(sub_str_index('aaaaab', 'aaab')) #! BREAKS! No back-tracking

# Neetcode's solution

class Solution:
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            # for j in range(len(needle)):
            #     if haystack[i + j] != needle[j]:
            #         break
            #     if j == len(needle - 1):
            #         return i
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
