# https://leetcode.com/problems/balanced-binary-tree/
# The same as hwk problem 5-4
"""
Let's say a binary tree is "super balanced" if the difference 
between the depths of any two leaf nodes is at most one.
Write a function to check if a binary tree is "super balanced".
"""

### THOUGHTS TAKEN FROM 5-4 ###
"""
We can utilize a dfs and keep track of the heights everytime we hit a leaf node.
Then if the difference of heights ever reaches more than one, we can determine
the tree is not super balanced.
"""

### Sudo Code ###
"""
Traverse our tree with dfs keeping track of our height.
We log our height after reaching a leaf node.
If our height ever reaches more or less than one level compared to our
logged heights, then we return False
else if we make it through our entire dfs, then we return True.
"""

### Code ###
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def checkBalance(self, root):
        self.balanced = True
        def dfs(root):
            if root:
                leftCount = dfs(root.left)
                rightCount = dfs(root.right)
                if abs(leftCount-rightCount)>1:
                    self.balanced = False
                return max(leftCount, rightCount)+1
            return 0
        dfs(root)
        return self.balanced

### Test Code ###
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print(tree.checkBalance(tree))

tree1 = TreeNode(1, TreeNode(2, TreeNode(3)))
print(tree1.checkBalance(tree1))