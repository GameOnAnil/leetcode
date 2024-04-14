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
        res = [0]
        def dfs(node,isLeft:bool,res):
            if not node:
                return
            if isLeft and not node.left and not node.right:
                res[0]+=node.val
                return
            dfs(node.left,True,res)
            dfs(node.right,False,res)
        dfs(root,False,res)
        return res[0]