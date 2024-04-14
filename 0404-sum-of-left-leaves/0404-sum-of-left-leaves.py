# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, isLeft: bool):
            if not node:
                return 0
            if isLeft and not node.left and not node.right:
                return node.val
            left = dfs(node.left, True)
            right = dfs(node.right, False)
            return left + right

        return dfs(root, False)
