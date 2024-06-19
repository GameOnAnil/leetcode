class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def no_of_bloom(mid):
            blooms = 0
            count = 0
            for i in bloomDay:
                if i <= mid:
                    count += 1
                else:
                    count = 0
                if count == k:
                    blooms += 1
                    count = 0
            return blooms

        start, end = 0, max(bloomDay)
        res = -1

        while start <= end:
            mid = (start + end) // 2
            if no_of_bloom(mid) >= m:
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res
