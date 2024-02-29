class Solution:
    def minInterval(self, iv: List[List[int]], queries: List[int]) -> List[int]:
        iv = sorted(iv)[::-1]
        h = []
        res = {}
        for q in sorted(queries):
            while iv and iv[-1][0] <= q:
                s, e = iv.pop()
                if q <= e:
                    heapq.heappush(h, [e - s + 1, e])
            while h and h[0][1] < q:
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]
