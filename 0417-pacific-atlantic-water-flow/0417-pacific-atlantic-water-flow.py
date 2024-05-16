class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        p_set, a_set = set(), set()

        def dfs(r, c, my_set):
            my_set.add((r, c))
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dx, dy = r + x, c + y
                if (
                    dx in range(rows)
                    and dy in range(cols)
                    and (dx, dy) not in my_set
                    and heights[dx][dy] >= heights[r][c]
                ):
                    dfs(dx, dy, my_set)

        # traverse pacific
        for i in range(rows):
            dfs(i, 0, p_set)
            dfs(i, cols - 1, a_set)
        for j in range(cols):
            dfs(0, j, p_set)
            dfs(rows - 1, j, a_set)
        # traverse atlantic
        return list(p_set & a_set)
