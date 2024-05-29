class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                rad.append(i)
            else:
                dire.append(i)
        n = len(senate) + 1
        while rad and dire:
            if rad[0] < dire[0]:
                dire.popleft()
                rad.popleft()
                rad.append(n)
                n+=1
            else:
                dire.popleft()
                rad.popleft()
                dire.append(n)
                n+=1
        return "Radiant" if len(rad) > 0 else "Dire"


        