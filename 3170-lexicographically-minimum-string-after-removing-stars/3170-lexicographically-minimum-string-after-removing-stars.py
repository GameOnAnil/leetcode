class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        indices = defaultdict(list)
        q = []
        heapq.heapify(q)
        for i, c in enumerate(s):
            if c == "*":
                s[i]=""
                curr = heapq.heappop(q)
                index = indices[curr[0]].pop()
                s[index] = ''
                if len(indices[curr[0]]) > 0:
                    heapq.heappush(q,(curr[0],curr[1]))
            else:
                indices[c].append(i)
                if len(indices[c]) == 1:
                    heapq.heappush(q,(c,i))

        return "".join(s)
            
        