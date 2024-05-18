# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        res = [0]
        def dfs(node,cur_max):
            if not node:
                return
            if node.val >=cur_max:
                res[0]+=1
                cur_max = node.val
            dfs(node.left,cur_max)
            dfs(node.right,cur_max)
        dfs(root,float("-inf"))
        return res[0]
        