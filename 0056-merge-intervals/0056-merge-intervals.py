class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]
        for s, e in intervals[1:]:
            curEnd = res[-1][1]
            if s <= curEnd:
                res[-1][1] = max(e, curEnd)
            else:
                res.append([s, e])
        return res
