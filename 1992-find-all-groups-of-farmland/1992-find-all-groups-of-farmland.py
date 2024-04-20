class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        def rightDirection(r,c):
            if (r not in range(rows) or c not in range(cols) or land[r][c]!=1):
                return 0
            land[r][c]="#"
            land[r+1][c]="#"
            return 1 + rightDirection(r,c+1)
        def botDirection(r,c):
            if (r not in range(rows) or c not in range(cols) or land[r][c]!=1):
                return 0
            land[r][c]="#"
            land[r][c+1]="#"
            return 1 + botDirection(r+1,c)
        res = []
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    land[r][c]="#"
                    right = rightDirection(r,c+1)
                    bot = botDirection(r+1,c)
                    res.append([c,r,c+bot,r+right])
        return res


        