class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        N = len(arrays)
        a, b = float("inf"), float("-inf")
        curr = 0
        for arr in arrays:
            if a == float("inf") or b == float("-inf"):
                a = min(a, arr[0])
                b = max(b, arr[-1])
                continue
            res = max(res, abs(arr[0] - b))
            res = max(res, abs(a - arr[-1]))
            a = min(a, arr[0])
            b = max(b, arr[-1])
        return res
