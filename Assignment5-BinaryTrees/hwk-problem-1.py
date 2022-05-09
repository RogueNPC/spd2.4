# https://leetcode.com/problems/invert-binary-tree/
# NOTE: I've changed the problem to this leetcode problem because
# the original question was too vague (in what way are we traversing though this tree?).
"""
Given the root of a binary tree, invert the tree, and return its root.

Example: Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
"""

### First Thoughts ###
"""
We could traverse through the binary tree recursively and once we hit a leaf node,
we will reverse the parent's two children node pointers.
"""

### Sudo Code ###
"""
Base case: when we hit an empty node return
Recursive case: we traverse through the left node, then the right node
we will then exchange the positions of the left and right nodes as we return.
"""

### Code ###
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root:
        
        root.left, root.right = root.right, root.left

        if root.left:
            invertTree(root.left)
        if root.right:
            invertTree(root.right)
    
    return root

# Helper function to print all nodes of a given level from left to right
def printLevel(root, level):
    if root is None:
        return False
 
    if level == 1:
        print(root.val, end=' ')
        return True
 
    left = printLevel(root.left, level - 1)
    right = printLevel(root.right, level - 1)
 
    return left or right
 
 
# Helper function to print level order traversal of a given binary tree
def levelOrderTraversal(root):
    level = 1
 
    while printLevel(root, level):
        level += 1

### Test Code ###
"""
Example: Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
"""
tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
levelOrderTraversal(tree)
print()
levelOrderTraversal(invertTree(tree))
print()
