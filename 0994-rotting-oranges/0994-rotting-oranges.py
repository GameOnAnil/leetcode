class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        res = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        while q and fresh > 0:
            print(q,fresh)
            for _ in range(len(q)):
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dx,dy in directions:
                    row, col = r+dx,c+dy
                    if (row not in range(ROWS) or col not in range(COLS) or grid[row][col] != 1):
                        continue
                    fresh-=1
                    grid[row][col] = 2
                    q.append((row,col))
            res+=1
        return res if (fresh== 0) else -1