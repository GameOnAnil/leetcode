class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        data = defaultdict(list)
        for n1,n2 in edges:
            data[n1].append(n2)
            data[n2].append(n1)
        seen = set()
        def dfs(node,seen):
            if node == destination:
                return True
            if node in seen:
                return False
            seen.add(node)
            for i in data[node]:
                if dfs(i,seen):
                    return True
            return False
        return dfs(source,seen)


        