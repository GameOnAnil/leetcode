class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(path, i):
            if len(path) == k:
                res.append(path[::])
                return
            for j in range(i, n + 1):
                if j in path:
                    continue
                dfs(path + [j], j + 1)

        dfs([], 1)
        return res
