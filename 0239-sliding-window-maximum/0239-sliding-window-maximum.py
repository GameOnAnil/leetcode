class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        res = []
        q = collections.deque()
        while r < len(nums):
            # Remove all item less than current from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # Remove item outside of the window
            if l > q[0]:
                q.popleft()
            # When r hits the window end add to output
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
