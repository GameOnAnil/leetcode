# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return (0, 0)

            l_size, l_coin = dfs(node.left)
            r_size, r_coin = dfs(node.right)

            size = 1 + l_size + r_size
            coins = node.val + l_coin + r_coin
            self.res += abs(size - coins)

            return (size, coins)

        dfs(root)
        return self.res
