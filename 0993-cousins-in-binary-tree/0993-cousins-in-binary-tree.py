# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append((root, None))
        depth = 0
        res = []
        while q:
            for _ in range(len(q)):
                curr, parent = q.popleft()
                if curr.val == x or curr.val == y:
                    res.append((parent, depth))
                if curr.left:
                    q.append((curr.left, curr))
                if curr.right:
                    q.append((curr.right, curr))
            depth += 1
        i = res[0]
        j = res[1]
        return i[0] != j[0] and i[1] == j[1]
