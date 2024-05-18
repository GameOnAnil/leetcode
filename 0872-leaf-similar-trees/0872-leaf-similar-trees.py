# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,path):
            if not node.left and not node.right:
                path.append(node.val)
                return
            if node.left:
                dfs(node.left,path)
            if node.right:
                dfs(node.right,path)
        res1 = []
        res2 = []
        dfs(root1,res1)
        dfs(root2,res2)
        return res1 == res2
        