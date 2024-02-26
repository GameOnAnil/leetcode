class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, sub: List[int], total: int):
            if target == total:
                res.append(sub[::])
                return
            if i >= len(candidates) or total > target:
                return
            sub.append(candidates[i])
            dfs(i, sub, total + candidates[i])
            sub.pop()
            dfs(i + 1, sub, total)

        res = []
        dfs(0, [], 0)
        return res
