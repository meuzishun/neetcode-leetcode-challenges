# My solution

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def is_palindrome(linked_list):
    arr = []
    
    node = linked_list.head
    
    while node:
        arr.append(node.data)
        node = node.next
    
    for i in range(len(arr) // 2):
        mirror_i = (i + 1) * -1
        
        if arr[i] != arr[mirror_i]:
            return False
    
    return True

print(is_palindrome(LinkedList([1, 2, 2, 1])))
print(is_palindrome(LinkedList([1, 2, 1])))
print(is_palindrome(LinkedList([1, 2])))

# Neetcode's 1st solution

class Solution1:
    def isPalindrome(self, head):
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

# Neetcode's 2nd solution

class Solution2:
    def isPalindrome(self, head):
        fast = head
        slow = head
        
        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True