# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        print(root)
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
        