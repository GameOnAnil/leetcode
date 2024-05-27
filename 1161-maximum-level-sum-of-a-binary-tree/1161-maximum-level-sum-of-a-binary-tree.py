# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res,level, curr_max = 0, 1, float("-inf")
        q = deque()
        q.append(root)
        while q:
            curr_sum = 0
            for _ in range(len(q)):
                curr = q.popleft()
                curr_sum+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if curr_sum >curr_max:
                res = level
                curr_max = curr_sum
            level+=1
        return res


        