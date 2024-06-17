class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(math.sqrt(c))
        
        while l <= r:
            s_sum = l*l + r*r
            if (s_sum)==c:
                return True
            elif s_sum > c:
                r-=1
            else:
                l+=1
        return False
        