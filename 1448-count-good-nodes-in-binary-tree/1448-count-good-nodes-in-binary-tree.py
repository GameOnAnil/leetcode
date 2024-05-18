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
        self.res = 0

        def dfs(node,path):
            if not node:
                return
            path.append(node.val)
            if node.val == max(path):
                self.res+=1
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        curr = []
        dfs(root,curr)
        return self.res
        