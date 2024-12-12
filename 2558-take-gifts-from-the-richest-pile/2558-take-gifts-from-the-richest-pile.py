class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = [-g for g in gifts]
        heapq.heapify(q)

        for _ in range(k):
            curr = heapq.heappop(q)
            heapq.heappush(q,-int(sqrt(-curr)))

        return -sum(q)

        