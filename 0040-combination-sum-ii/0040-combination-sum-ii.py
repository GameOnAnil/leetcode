class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dfs(i, path, total):
            if target == total:
                res.append(path[::])
                return
            if i >= len(candidates) or total > target:
                return
            dfs(i + 1, path + [candidates[i]], total + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, path, total)

        res = []
        dfs(0, [], 0)
        return res
