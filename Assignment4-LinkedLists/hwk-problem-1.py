# No close Leetcode equivalent
"""
Given a singly-linked list, rearrange the nodes by interleaving 
the first half of the linked list with the second half.

Example: If the given linked list is A → B → C → D → E → F → G → H, 
    nodes should be rearranged so the list becomes A → C → E → G → B → D → F → H.
"""

### FIRST THOUGHTS ###
"""
Can we rearrange the linked list in place?  We can have one pointer go through the list 
visiting every other node and connecting them all while a second pointer goes through all the 
other nodes and creates a seperate linked list.  Then we can connect the first list with the second list.
"""

### Code ###
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def interleaveLinkedList(l1: ListNode) -> ListNode:
    if l1 == None:
        return []

    head = l1
    temp_list = ListNode()
    temp_head = temp_list

    while l1.next and l1.next.next:
        # creates new list of all nodes jumped over by iterator
        temp_list.next = ListNode(l1.next.val)
        temp_list = temp_list.next

        # iterates through every other node
        l1.next = l1.next.next
        l1 = l1.next
    
    # Checks for last node when passing lists with even # of nodes
    if l1.next:
        temp_list.next = ListNode(l1.next.val)

    # Connects both lists
    l1.next = temp_head.next

    return head

# Helper function to print out nodes
def printList(l1):
    while l1:
        print(l1.val, end=' ')
        l1 = l1.next
    print()

### TEST CODE ###
l1 = ListNode('A', ListNode('B', ListNode('C')))
l2 = ListNode('A', ListNode('B', ListNode('C', ListNode('D'))))
printList(interleaveLinkedList(l1))
printList(interleaveLinkedList(l2))

l3 = ListNode('A', ListNode('B', ListNode('C', ListNode('D', ListNode('E', ListNode('F', ListNode('G', ListNode('H'))))))))
printList(interleaveLinkedList(l3))