# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node,steps,is_left):
            if not node:
                return
            self.res = max(self.res,steps)
            if is_left:
                dfs(node.left,steps+1,False)
                dfs(node.right,1,True)
            else:
                dfs(node.right,steps+1,True)
                dfs(node.left,1,False)
        
        dfs(root,0,True)
        dfs(root,0,False)
        return self.res



        