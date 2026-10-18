# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def depth(node):
            if node is None:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            # BLANK 1: update self.best using left and right
            self.best = max(self.best, left + right)
            return max(left, right) + 1
            # BLANK 2: return this node's depth (you already know this one)

        

        depth(root)
        return self.best

        