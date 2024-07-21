# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r,s):
            if (not r and s) or (not s and r):
                return False
            if not s and not r:
                return True
            if r.val != s.val:
                return False
            return isSame(r.left,s.left) and isSame(r.right,s.right)
        
        def dfs(r,s):
            if not r:
                return False
            if r.val == s.val and isSame(r,s):
                return True
            return dfs(r.left,s) or dfs(r.right,s)
        return dfs(root,subRoot)
        