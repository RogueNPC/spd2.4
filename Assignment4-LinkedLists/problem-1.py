# No close Leetcode equivalent
"""
Given a single-linked list, find the middle value in the list.

NOTE: I will assume that we will want to find the middle values 
in the event there is an even number of values.
"""

### First Thoughts ###
"""
Traverse through the linked list and place values into an array, find the middle value.
Not the best approach seeing as that will involve making extra memory for an array.

Traverse through the linked list and count how many nodes there are with a counter.
Then traverse through the linked list again by the counter / 2.
This is the cleanest way I can think of solving this problem.
"""

### Sudo Code ###
"""
Create counter at 0
Then travel though the linked list while incrementing the counter after every node.
At the end of the list, divide the counter by 2 and traverse through the list
by the number of times the counter says.

NOTE: While coding, I realized I can just increment the counter and traverse through the list
skipping every other node to simulate dividing the counter by 2.
"""

### Code ###
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddleValue(l1):
    if l1 == []:
        return None

    head = l1
    counter = 0

    while l1.next and l1.next.next:
        counter += 1
        l1 = l1.next.next
    while counter > 0:
        head = head.next
        counter -= 1

    # returns both middle values if list has even number of nodes
    if l1.next and not l1.next.next:
        lst = [head.val, head.next.val]
        return lst

    return head.val


### Test code ###
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(2, ListNode(4))))
l3 = []

print(findMiddleValue(l1))
print(findMiddleValue(l2))
print(findMiddleValue(l3))