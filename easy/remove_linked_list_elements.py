# My solution

def remove_element(val, node):
    head = node
    curr = node
    prev = None
    
    while curr:
        if curr.value == val:
            if prev:
                prev.next = curr.next
            else:
                head = curr
        else:
            prev = curr
        
        curr = curr.next
    
    return head

# Neetcode's solution

# Creating a dummy node that will always point to the head

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        
        while curr:
            nxt = curr.next
            
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            
            curr = nxt
        
        return dummy.next