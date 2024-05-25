class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dist = {}
        v = defaultdict(int)
        res=[0] * len(queries)
        index = 0
        
        def updateColor(i):
            prev = dist.get(i)
            v[prev]-=1
            if v.get(prev) <=0:
                del v[prev]
            
        for i,j in queries:
            if (i in dist):
                updateColor(i)
            v[j]+=1
            dist[i] = j
            res[index]=len(v.values())
            index+=1
        return res