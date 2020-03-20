# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        if tree1 == None or tree2 == None:
            return False
    
        return tree1.val == tree2.val and self.isMirror(tree1.right, tree2.left) and self.isMirror(tree1.left, tree2.right)

    def isSymmetric2(self, root: TreeNode) -> bool:
        stack = [root, root]

        while len(stack) > 0:
            t1 = stack.pop()
            t2 = stack.pop()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)

        return True
