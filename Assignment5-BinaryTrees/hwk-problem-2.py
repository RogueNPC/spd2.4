# No close Leetcode equivalent
"""
Given a binary search tree containing integers and a target integer, 
come up with an efficient way to locate two nodes in the tree 
whose sum is equal to the target value.
"""

### First Thoughts ###
"""
Like the normal two sum problem in the array set, we can utilize a normal binary search
algorithm to go through all the nodes.  As we traverse through the tree, we
create a running list of values that would add up with one of our previous nodes.
In this way, we can traverse through the tree once to locate two nodes in the tree
whose sum equals a target value.
"""

### Code ###
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

target_nums = []
def searchTree(root, target):
    if root:
        if root.val in target_nums:
            print(root.val, target - root.val)

        target_nums.append(target - root.val)

        if root.left:
            searchTree(root.left, target)
        if root.right:
            searchTree(root.right, target)

### Test Code ###
tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
searchTree(tree, 12)