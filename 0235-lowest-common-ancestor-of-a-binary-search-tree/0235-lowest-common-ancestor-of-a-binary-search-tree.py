# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root
        while True:
            if temp.val < q.val and temp.val < p.val:
                temp = temp.right
            elif temp.val > q.val and temp.val > p.val:
                temp = temp.left
            else:
                return temp
            
        