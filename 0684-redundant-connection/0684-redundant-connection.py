class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)


        def findRoot(n):
            p = par[n]
            while p !=par[p]:
                currParent = par[p]
                par[p] = par[currParent]
                p = currParent
            return p

        def union(n1,n2):
            p1,p2 = findRoot(n1), findRoot(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                rank[p1]+=1
                par[p2] = p1
            else:
                rank[p2]+=1
                par[p1] = p2

            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]


        