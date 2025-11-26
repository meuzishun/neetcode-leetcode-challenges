# My solution

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, arr):
        self.head, curr, prev = None, None, None
        
        for i, val in enumerate(arr):
            curr = Node(val, None)
            
            if not self.head:
                self.head = curr
                
            if prev:
                prev.next = curr
            
            prev = curr
            
    def print_list(self):
        node = self.head
        
        while node:
            if node.next:
                print(node.val, '-->')
            else:
                print(node.val)
            node = node.next
            
linked_list = LinkedList(['a', 'b', 'b', 'c', 'd', 'd', 'e'])
linked_list.print_list()

def remove_dups(head):
    prev = head
    curr = head.next
    
    while curr:
        while curr.val == prev.val:
            curr = curr.next
        
        prev.next = curr
        tmp = curr
        curr = curr.next
        prev = tmp
    
    return head

remove_dups(linked_list.head)
linked_list.print_list()

# Neetcode's solution

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head