# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            curr = -1
            for i in range(len(q)):
                c = q.popleft()
                curr = c.val
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            res.append(curr)
        return res
