# My solution

def intersection_of_two_linked_lists(headA, headB):
    hist = set()
    
    node = headA
    
    while node:
        hist.add(node)
        node = node.next
        
    node = headB
    
    while node:
        if node in hist:
            return node
        node = node.next
    
    return None

# Neetcode's solution (study this more... its a good one)

class Solution:
    def getIntersectionNode(self, headA, headB):
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
