# No close Leetcode equivalent
"""
Given a singly-linked list and an integer k, find the value in the kth-to-last node.

Example: If the given linked list is 1->2->8->3->7->0->4 and k = 3,
         then the function should return 7 (the 3rd element from the end)

Assumption: k is greater than 0 and exists in the linked list.
"""

### FIRST THOUGHTS ###
"""
A brute force method would be to traverse through the linked list, 
turning it into an array and returning the -kth element of the array.  
That would be a time complexity of O(n) and a space complexity of O(n).

A better solution would involve not creating an extra list.
We can do this iteratively with two pointers if we stagger them a
distance of k - 1 apart and move both pointers until one pointer
hits the end of the list.  The other pointer should be the
kth-to-last node.
"""

### SUDO CODE ###
"""
Create target pointer and end pointer at head node.
Move end pointer through the linked list k-1 times.
Move target and end pointer through linked list 
until end pointer hits end of list.
Return target pointer value.
"""

### CODE ###
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findKthLast(l1: ListNode, k: int) -> int:
    if l1 == None:
        return None
    
    target, end = l1, l1
    
    for _ in range(k-1):
        end = end.next

    while end and end.next:
        target = target.next
        end = end.next
    
    return target.val

### TEST CODE ###
l1 = ListNode(1, ListNode(2, ListNode(8, ListNode(3, ListNode(7, ListNode(0, ListNode(4)))))))
k = 3
print(findKthLast(l1, k))

l2 = ListNode(1, ListNode(3, ListNode(4)))
k1 = 1
print(findKthLast(l2, k1))