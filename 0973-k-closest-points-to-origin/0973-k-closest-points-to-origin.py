class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points,key = lambda P:P[0]**2+P[1]**2)[:k]
         
