class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        dq = deque()
        res = [None] * len(deck)
        for i in range(len(deck)):
            dq.append(i)
        for i in range(len(deck)):
            res[dq.popleft()] = deck[i]
            if dq:
                dq.append(dq.popleft())
        return res
        