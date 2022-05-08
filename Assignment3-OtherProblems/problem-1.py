# https://leetcode.com/problems/merge-k-sorted-lists/
# The same as hwk problem 4-3
"""
Given an array of k singly-linked lists, each of whose values are in sorted order, 
combine all nodes (do not create new nodes) into one singly-linked list with all values in order.
"""

### THOUGHTS TAKEN FROM 4-3 ###
"""
If we know how to sort two sorted linked lists, then in order to sort k linked lists,
we just have to sort the linked lists two at a time until only one remains.

We can do this using a merge sort algorithm to split our parings into generally equal lists.
"""

### CODE ###
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function that we call
def mergeKLists(lists) -> ListNode:
    return getLists(lists, 0, len(lists) - 1)
    
# Helper function merges our two lists obtained by getLists()
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

# Helper function completes the merge algorithm
# (splitting in half until pairs form, merging those pairs, and returning one big list)
def getLists(lists, start, end):
    if end < start:
        return []
    if start == end:
        return lists[start]
    # Recursively splits the list in half until there are two lists where it merges the two lists together
    return mergeTwoLists(getLists(lists, start, start + (end - start)//2), getLists(lists, start + (end - start)//2 + 1, end))

# Helper function to print out nodes
def printList(l1):
    while l1:
        print(l1.val, end=' ')
        l1 = l1.next
    print()

### TEST CODE ###
lists = [ListNode(1, ListNode(4, ListNode(5))),
         ListNode(1, ListNode(3, ListNode(4))),
         ListNode(2, ListNode(6))]
printList(mergeKLists(lists))

lists1 = []
print(mergeKLists(lists1))

lists2 = [[]]
print(mergeKLists(lists2))