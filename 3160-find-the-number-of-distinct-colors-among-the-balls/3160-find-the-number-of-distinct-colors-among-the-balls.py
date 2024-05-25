class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        seen = defaultdict(int)
        colors = defaultdict(int)
        res=[0] * len(queries)
        index = 0
        
        def updateColor(i):
            prev = seen.get(i)
            colors[prev]-=1
            if colors.get(prev) <=0:
                del colors[prev]
            
        for i,j in queries:
            if i in seen:
                updateColor(i)
            colors[j]+=1
            seen[i] = j
            res[index]=len(colors)
            index+=1
        return res