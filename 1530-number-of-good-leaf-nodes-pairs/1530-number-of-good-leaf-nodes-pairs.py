# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = [0]

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            curr = left + right
            for i in left:
                for j in right:
                    if (i + j) <= distance:
                        res[0] += 1
            return [c + 1 for c in curr]

        dfs(root)
        return res[0]
