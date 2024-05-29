class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        carry = 0
        res = 0
        for i in range(len(s)-1,0,-1):
            curr = int(s[i]) + carry
            if curr % 2 == 1:
                carry = 1
                res+=2
            else:
                res+=1

        return res + carry
        