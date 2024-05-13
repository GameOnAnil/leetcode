class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        data = []
        for i in range(len(quality)):
            data.append((quality[i], wage[i] / quality[i]))
        data.sort(key=lambda x: x[1])

        maxHeap = []
        total_quality = 0
        res = float("inf")
        for q, r in data:
            heapq.heappush(maxHeap, -q)
            total_quality += q

            if len(maxHeap) > k:
                m = heapq.heappop(maxHeap)
                total_quality+=m

            if len(maxHeap) == k:
                res = min(res, total_quality * r)

        return res
