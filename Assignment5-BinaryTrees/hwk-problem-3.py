# https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
Given a binary tree containing numbers, 
find the maximum sum path (the path that has the largest sum of node values). 
The path may start and end at any node in the tree.
"""

### First Thoughts ###
"""
Given that in a binary search tree, the path that reaches the most nodes
involves a inorder depth-first search.  

Given that if our binary tree branches out after the root node, 
we'll have to choose between coming from the right or the left nodes of each subsequent parent node.  
We can choose left or right by comparing which left or right nodes after our root node yields the higher value.

If all the nodes in our tree were positive, then all we would have to do is add up all of our nodes, 
however because some nodes can be negative, we must also compare whether or not 
placing a specific node in our path will decrease our current total sum.
"""

### Sudo Code ###
"""
Traverse through our nodes in an inorder dfs, if we hit a non-existent node, we give it a val of 0.
At every step of our dfs, we compare the left and right node values for the highest value.
We also have to check whether the higher of the two are greater than 0.
If they are, then we add it to our path sum.
At the end of the dfs, we return our path sum.
"""

### Code ###
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def maxPathSum(self, root):
        self.ans = -1001
        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                ans = root.val
                ans = max(ans, l + ans)
                ans = max(ans, r + ans)
                self.ans = max(self.ans, ans)
                return max(root.val, root.val + max(l, r))
            else:
                return 0
                
        dfs(root)   
        return self.ans

### Test Code ###
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print(tree.maxPathSum(tree))

tree1 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(tree1.maxPathSum(tree1))