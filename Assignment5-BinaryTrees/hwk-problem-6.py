# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/ (require premium)
"""
Given a binary search tree, convert it into a sorted doubly-linked list 
by modifying the original tree nodes (do not create new nodes).
"""

### First Thoughts ###
"""
In order to convert our bst into a doubly-linked list, we have to understand what it is we'll be doing.
The left nodes of our tree will be pointing to the node before and the right nodes will be
pointing to node after in an inorder depth-first search traversal.
"""

### Code ###
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoubleList(root):
    if not root:
        return None
    
    nodes = []

    def inorder(root, results):
        if not root:
            return
                
        inorder(root.left, results)        
        results.append(root)
        inorder(root.right, results)

    inorder(root, nodes)
    
    head = nodes[0]
    prev = head

    for node in nodes[1:]:
        node.left = prev
        prev.right = node
        prev = node
        
    prev.right = head
    head.left = prev
    
    return head

# Helper function to print out nodes
def printList(node):
    head = node
    print(node.val, end=' ')
    while node.right != head:
        node = node.right
        print(node.val, end=' ')
    print()

# Helper function to print out nodes backwards
def printListBackwards(node):
    head = node
    print(node.val, end=' ')
    while node.left != head:
        node = node.left
        print(node.val, end=' ')
    print()

### Test Code ###
tree = TreeNode(2, TreeNode(1), TreeNode(3))
tree = treeToDoubleList(tree)
printList(tree)
printListBackwards(tree)

tree1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
tree1 = treeToDoubleList(tree1)
printList(tree1)
printListBackwards(tree1)