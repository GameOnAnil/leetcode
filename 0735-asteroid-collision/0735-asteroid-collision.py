class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        res = []
        for a in ast:
            while res and a < 0 and res[-1] > 0:
                if res[-1] + a < 0:
                    res.pop()
                elif res[-1] + a >0:
                    break
                else:
                    res.pop()
                    break
            else:
                res.append(a)
        return res
     