class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        
        seen = set([(0, 0)])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(n, count, stack):
            if n == 0:
                return count
            new_list = []
            for l, r in stack:
                for dx, dy in direction:
                    x, y = l + dx, r + dy
                    if (x, y) not in seen:
                        seen.add((x, y))
                        new_list.append((x, y))
            return bfs(n - 1, count + len(new_list), new_list)

        return bfs(n - 1, 1, [(0, 0)])
