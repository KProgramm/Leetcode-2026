# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #need to update two things: max bent path (best), depth of right and left

        best = 0

        def depth(node):
            nonlocal best
            #base case
            if not node:
                return 0
            right = depth(node.right)
            left = depth(node.left)
            best = max(best, right + left)
            return max(right, left) + 1

        
        depth(root)
        return best

        