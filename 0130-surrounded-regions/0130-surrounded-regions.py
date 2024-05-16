class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        good = set()
        q = deque()
        def bfs():
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    good.add((r,c))
                    for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
                        dx,dy = r+x, c+y
                        if (dx in range(rows) and dy in range(cols) and board[dx][dy] == "O" and (dx,dy) not in good):
                            q.append((dx,dy))

        for i in range(rows):
            if board[i][0]=="O":
                q.append((i,0))
                good.add((i,0))
            if board[i][cols-1]=="O":
                q.append((i,cols-1))
                good.add((i,cols-1))
        for j in range(cols):
            if board[0][j]=="O":
                q.append((0,j))
                good.add((0,j))
            if board[rows-1][j]=="O":
                q.append((rows-1,j))
                good.add((rows-1,j))
        bfs()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in good:
                    board[i][j] = "X"                    
        