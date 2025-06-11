# My attempt

def reverse_linked_list(linked_list):
    curr = linked_list.head
    prev = None
    
    while curr.next:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return curr

# Neetcode's solution 1

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
# Neetcode' solution 2

class Solution2:
    def reverseList(self, head):
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead

# From comments
def reverseListRecursive(self, head):
    def reverse(cur, prev):
        if cur is None:
            return prev
        else:
            next = cur.next
            cur.next = prev
            return reverse(next, cur)

    return reverse(head, None)

# create a linked list class for testing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
        
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

test = Solution2()
test.reverseList(linked_list.head)