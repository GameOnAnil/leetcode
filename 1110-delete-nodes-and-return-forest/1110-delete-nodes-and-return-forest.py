# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []

        def dfs(node):
            if not node:
                return None
            # process left & right
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            # handle delete case
            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None
            return node

        root = dfs(root)
        if root:
            res.append(root)
        return res