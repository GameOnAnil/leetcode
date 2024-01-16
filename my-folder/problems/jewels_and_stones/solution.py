class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jew = list(jewels)
        sto = list(stones)
        for i in range(0,len(jew)):
            for j in range(0,len(sto)):
                if jew[i] == sto[j]:
                    count += 1
        return count

        