# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #base case: bro i rly gotta study this:
        if not root:
            return []

        tree_right = []
        q = deque([root])

        while q:
            original_length = len(q)
            for i in range(original_length):
                node = q.popleft()
                if i == original_length - 1:
                    tree_right.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return tree_right
        