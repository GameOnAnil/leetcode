class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col =[set() for i in range(9)]
        row = [set() for i in range(9)]
        grid = [set() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c == ".":continue
                g = (i//3)*3 + j//3
                if c in row[i] or c in col[j] or c in grid[g]:
                    return False
                row[i].add(c)
                col[j].add(c)
                grid[g].add(c)
        return True