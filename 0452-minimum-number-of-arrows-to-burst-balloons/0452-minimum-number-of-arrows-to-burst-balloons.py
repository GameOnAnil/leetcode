class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: p[1])
        res, arrow = 0, 0
        for (start,end) in points:
            if res == 0 or start > arrow:
                res +=1
                arrow = end
        return res
        