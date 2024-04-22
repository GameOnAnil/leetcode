# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        q = deque()
        q.append(root)

        while len(q) > 0:
            N = len(q)
            temp = []
            for _ in range(N):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    temp.append(curr.left.val)
                else:
                    temp.append(None)
                if curr.right:
                    q.append(curr.right)
                    temp.append(curr.right.val)
                else:
                    temp.append(None)
            if temp and temp!=temp[::-1]:
                return False
                
        return True
