class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for p in points:
            dist = -(p[0] * p[0] + p[1] * p[1])
            heapq.heappush(maxheap, (dist, p))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [m[1] for m in maxheap]
