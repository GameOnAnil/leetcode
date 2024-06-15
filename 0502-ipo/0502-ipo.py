class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pnc  = list(zip(capital,profits))
        curr_max = []
        heapq.heapify(pnc)
        while k > 0:
            if pnc and pnc[0][0] > w:
                return w
            while pnc and pnc[0][0] <=w:
                curr = heapq.heappop(pnc)
                heapq.heappush(curr_max,(-curr[1],-curr[0]))
            if not curr_max:
                return w
            m = heapq.heappop(curr_max)
            w-=m[0]
            k-=1
        return w
        