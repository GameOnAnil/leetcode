class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:
            return deck
        deck.sort()
        n = len(deck)
        dq = collections.deque()
        res = [None]* n
        for i in range(n):
            dq.append(i)
        for d in deck:
            index = dq.popleft()
            res[index] = d
            if dq:
                dq.append(dq.popleft())
        return res


        

        