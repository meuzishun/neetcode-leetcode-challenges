# I read the prompt wrong!

def merge_two_sorted_lists(list1, list2):
    result = []
    
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            result.append(list1[0])
            list1 = list1[1:]
        else:
            result.append(list2[0])
            list2 = list2[1:]
            
    if len(list1) > 0:
        result.extend(list1)
        
    if len(list2) > 0:
        result.extend(list2)
        
    return result        

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My REAL attempt

def merge_two_sorted_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = ListNode(list1.val)
        else:
            tail.next = ListNode(list2.val)
    
    if list1.val:
        tail.next = list1
        
    if list2.val:
        tail.next = list2
        
    return tail
            
# Neetcode's solution

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next