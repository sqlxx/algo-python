class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def balancedAndHeight(root):
            if not root:
                return 0
            
            left_height = balancedAndHeight(root.left)
            if left_height == -1:
                return -1
        
            right_height = balancedAndHeight(root.right)
            
            
            if right_height == -1 or abs(left_height-right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1
                
        height = balancedAndHeight(root)
        return height != -1