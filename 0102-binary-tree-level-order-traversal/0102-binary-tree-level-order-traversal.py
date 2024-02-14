# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            visited = []
            for i in range(len(q)):
                l = q.popleft()
                if l:
                    visited.append(l.val)
                    q.append(l.left)
                    q.append(l.right)            
            if visited:
                res.append(visited)
        return res

        