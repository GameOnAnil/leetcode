class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dq = deque()
        for i in range(len(tickets)):
            dq.append(i)
        res = 0
        while tickets[k] > 0:
            index = dq.popleft()
            if tickets[index] > 0:
                tickets[index]=tickets[index]-1
                res+=1
            dq.append(index)
        return res

        