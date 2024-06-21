class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        grumpy = list(zip(grumpy,customers))
        res = 0

        for g,c in grumpy:
            if g == 0:
                res+=c

        l,r=0,minutes
        for i in range(minutes):
            if grumpy[i][0] == 1:
                res+=grumpy[i][1]
        curr = res
        while r < len(grumpy):
            if grumpy[l][0] == 1:
                curr-=grumpy[l][1]
            if grumpy[r][0] == 1:
                curr+=grumpy[r][1]
            res = max(curr,res)
            l+=1
            r+=1

        return res

        