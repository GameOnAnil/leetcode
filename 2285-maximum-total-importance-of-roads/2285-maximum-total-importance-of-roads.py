class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = defaultdict(int)
        data = defaultdict(int)

        for u, v in roads:
            count[u]+=1
            count[v]+=1
        index = n
        for k,v in sorted(count.items(),key=lambda x: x[1],reverse=True):
            data[k] = index
            index-=1

        res = 0
        for u,v in roads:
            curr = data[u]+data[v]
            res+=curr
        return res
        