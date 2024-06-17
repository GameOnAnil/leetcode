class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        l = 0
        while l*l < c:
            b = math.sqrt(c-l*l)
            if b == int(b):
                return True
            l+=1
        return False
        