# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path.append(str(node.val))
            if not node.left and not node.right:
                if not path:
                    return 0
                return int("".join(path))
            return dfs(node.left, path.copy()) + dfs(node.right, path.copy())

        return dfs(root, [])
