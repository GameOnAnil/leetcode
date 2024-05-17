# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        curr = prev = root
        temp = ListNode(curr.val)

        def dfs(node):
            if not node:
                return node
            node.left  = dfs(node.left)
            node.right = dfs(node.right)
            
            if not node.left and not node.right and node.val == target:
                return None
            return node

        return dfs(root)



        