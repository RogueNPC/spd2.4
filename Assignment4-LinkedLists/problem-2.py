# https://leetcode.com/problems/merge-two-sorted-lists/
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

### FIRST THOUGHTS ###
"""
Given that the two linked lists are sorted, we can traverse through each at the same time
and compare the values of both heads.  The lower of the values will be popped out of their
linked list and into the new merged linked list.  This will continue until both lists
are empty.
"""

### SUDO CODE ###
"""
While both of the lists still contain nodes, 
compare head node values and add the lower value into the new merged list.
Then move onto the lower value's next node and compare values again.
Continue until one of the lists are empty, then add all the nodes
from the remaining list.
"""

### CODE ###
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == [] and l2 == []:
        return []
    head = ListNode()
    point = head
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            point = point.next
            l1 = l1.next
        else:
            point.next = l2
            point = point.next
            l2 = l2.next
    while l1:
        point.next = l1
        point = point.next
        l1 = l1.next
    while l2:
        point.next = l2
        point = point.next
        l2 = l2.next
    return head.next


### Test Code ###
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

merged = mergeTwoLists(l1,l2)
merged_list = []
while merged:
    merged_list.append(merged.val)
    merged = merged.next
print(merged_list)