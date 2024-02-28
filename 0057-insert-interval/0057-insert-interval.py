class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        for i, old in enumerate(intervals):
            if newInterval[1] < old[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > old[1]:
                res.append(old)
            else:
                newInterval = [min(newInterval[0], old[0]), max(newInterval[1], old[1])]
        res.append(newInterval)
        return res
