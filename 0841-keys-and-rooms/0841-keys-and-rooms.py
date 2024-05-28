class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        seen = set()

        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for j in rooms[i]:
                dfs(j)

        for i in range(N):
            if i > 0 and i not in seen:
                return False
            for j in rooms[i]:
                dfs(j)
        return True


        