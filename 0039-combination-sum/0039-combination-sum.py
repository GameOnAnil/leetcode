class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, sub: List[int], total: int):
            if target == total:
                res.append(sub[::])
                return
            if i >= len(candidates) or total > target:
                return
            dfs(i, sub + [candidates[i]], total + candidates[i])
            dfs(i + 1, sub, total)

        res = []
        dfs(0, [], 0)
        return res
