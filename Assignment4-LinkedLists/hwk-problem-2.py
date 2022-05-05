# https://leetcode.com/problems/rotate-list/ (similar)
"""
Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.

Example: If the given linked list is A → B → C → D → E → F and k is 4, 
        nodes should be modified so the list becomes E → F → A → B → C → D.

Assumptions: k is positive and smaller than n, the length of the linked list.
"""

### FIRST THOUGHTS ###
"""
We can iterate throught the linked list k-1 times and simply make the next node our head node.
We will also have to make sure to remove the next poiner of our new end node.
"""

### SUDO CODE ###
"""
Traverse through our linked list until we hit the kth node.
Make the kth next node our head node.
Remove the next pointer of the kth node.
Continue traversing until we hit the end of the original list.
Make the last node point to our original first node.
Return our new head node.
"""

### CODE ###
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def rotateCounterClockwise(head: ListNode, k: int) -> ListNode:
    if k == 0:
        return head

    origin, point = head, head

    # Traverse through our linked list until we hit the kth node.
    for _ in range(k-1):
        point = point.next

    end = point

    # Make the kth next node our head node.
    new_head = point.next
    point = point.next

    # Remove the next pointer of the kth node.
    end.next = None

    # Continue traversing until we hit the end of the original list.
    while point and point.next:
        point = point.next

    # Make the last node of our original list point to our original first node.
    point.next = origin

    # Return our new head node.
    return new_head


# Helper function to print out nodes
def printList(l1):
    while l1:
        print(l1.val, end=' ')
        l1 = l1.next
    print()

### TEST CODE ###
l1 = ListNode('A', ListNode('B', ListNode('C')))
k = 1
printList(rotateCounterClockwise(l1, k))

l2 = ListNode('A', ListNode('B', ListNode('C', ListNode('D', ListNode('E', ListNode('F'))))))
k1 = 4
printList(rotateCounterClockwise(l2, k1))