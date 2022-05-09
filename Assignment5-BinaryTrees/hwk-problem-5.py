# https://leetcode.com/problems/validate-binary-search-tree/
"""
Given a binary tree, check whether it is a valid binary search tree (values in order).
"""

### First Thoughts ###
"""
Traversing through the tree, we can compare node values to the root value
and determine whether the left child is less than their parent and the right child
is greater than their parent.  We'll also have to determine whether they are less than
or greater than (whichever is appropriate) all earlier root nodes that existed before them.
"""

### Sudo Code ###
"""
Traverse through the tree recursively.
We track the min and max values that a node can be based on the root nodes we visit.
Return false if a node's value ever goes outside of the min or max values.
Return true if we complete the traversal.
"""

### Code ###
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def isValidBST(self, root):        
        def validate(root):       
            valid, min, max = True, root.val, root.val
            if root.left:
                valid, min, lmax = validate(root.left)
                valid &= lmax < root.val
            
            if not valid: 
                return valid, min, max
            
            if root.right:
                valid, rmin, max = validate(root.right)
                valid &= root.val < rmin
            
            return valid, min, max

        valid, _, _ = validate(root)

        return valid

tree = TreeNode(1, TreeNode(2), TreeNode(3))
print(tree.isValidBST(tree))

tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(tree1.isValidBST(tree1))