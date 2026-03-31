# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def depL(curr):
            n = 0
            while curr:
                n += 1
                curr = curr.left
            return n
        
        def depR(curr):
            n = 0
            while curr:
                n += 1
                curr = curr.right
            return n
        
        DL = depL(root.left)
        DR = depR(root.right)

        if DR == DL:
            return 2**(DL + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        