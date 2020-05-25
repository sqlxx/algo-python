# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
       
        if not root.left and not root.right:
            return sum == root.val
        
        result = False
        
        if  root.right:
            result = self.hasPathSum(root.right, sum - root.val)
            
        if result:
            return True
        elif root.left:
            return self.hasPathSum(root.left, sum - root.val)
        else:
            return False
            
            