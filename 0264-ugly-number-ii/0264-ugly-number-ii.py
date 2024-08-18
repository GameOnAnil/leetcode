class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = []
        seen = set()
        prime = [2,3,5]

        heapq.heappush(minHeap,1)
        seen.add(1)

        curr = 1
        for _ in range(n):
            curr = heapq.heappop(minHeap)
            for p in prime:
                nextUgly = curr * p
                if nextUgly not in seen:
                    heapq.heappush(minHeap,nextUgly)
                    seen.add(nextUgly)
        return curr

