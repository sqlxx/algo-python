# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        
        left_depth, right_depth = 0, 0
        left_traversal, right_traversal = [], []
        if root.left:
            left_traversal = self.levelOrderBottom(root.left)    
            left_depth = len(left_traversal)
        
        if root.right:
            right_traversal = self.levelOrderBottom(root.right)
            right_depth = len(right_traversal)

        depth = min(left_depth, right_depth)

        if left_depth > right_depth:
            primary = left_traversal

        else:
            primary = right_traversal
        

        for i in range(-1, -depth - 1, -1):
            primary[i] = left_traversal[i] + right_traversal[i]
            
        return primary + [[root.val]] 
