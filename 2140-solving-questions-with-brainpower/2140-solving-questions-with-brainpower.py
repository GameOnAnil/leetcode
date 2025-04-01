class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i):
            if i >= len(questions):
                return 0
            points, skip = questions[i]
            take = points + dfs(i + skip + 1)
            skip = dfs(i + 1)
            return max(take, skip)

        return dfs(0)
