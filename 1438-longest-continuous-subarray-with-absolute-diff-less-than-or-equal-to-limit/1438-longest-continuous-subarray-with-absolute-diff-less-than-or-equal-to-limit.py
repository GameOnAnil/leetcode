from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        sl = SortedList()
        l, res = 0, 0

        for r in range(N):
            sl.add(nums[r])
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[l])
                l += 1

            res = max(res, r - l + 1)
        return res
