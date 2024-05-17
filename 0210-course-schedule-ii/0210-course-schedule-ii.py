class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # Adj list
        for p in prerequisites:
            graph[p[0]].append(p[1])

        visited, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for p in graph[crs]:
                if dfs(p) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for n in range(numCourses):
            if dfs(n) == False:
                return []
        return res


        