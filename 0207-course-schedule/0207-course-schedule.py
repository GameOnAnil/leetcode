class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])

        visited, cycle = set(),set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for c in graph[course]:
                if dfs(c) == False:
                    return False
            cycle.remove(course)
            visited.add(course)

        for n in range(numCourses):
            if dfs(n) == False:
                return False

        return True
        