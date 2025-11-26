# My solution

def search_insert_position(array, target):
    for i, val in enumerate(array):
        if val > target:
            return i
        
        if val == target:
            return i
    
    return len(array)
        
# print(search_insert_position([1, 3, 5, 6], 5))
# print(search_insert_position([1, 3, 5, 6], 2))
# print(search_insert_position([1, 3, 5, 6], 7))

# Another try

def search_insert_position2(array, target):
    length = len(array)
    
    if length == 1 and array[0] > target:
        return 0
    
    if length == 1 and array[0] < target:
        return 1
    
    mid = length // 2
    
    if array[mid] == target:
        return mid
    
    if array[mid] > target:
        return search_insert_position2(array[:mid], target)
    
    if array[mid] < target:
        return mid + search_insert_position2(array[mid:], target)
    
print(search_insert_position2([1, 3, 5, 6], 5))
print(search_insert_position2([1, 3, 5, 6], 2))
print(search_insert_position2([1, 3, 5, 6], 7))

# Neetcode's solution

class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
            
            if target < nums[mid]:
                r = mid - 1

        return l
