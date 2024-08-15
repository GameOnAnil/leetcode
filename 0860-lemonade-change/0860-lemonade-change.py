class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        seen = defaultdict(int)

        for i in bills:
            if i == 5:
                seen[i]+=1
            elif i == 10:
                if seen[5] <=0:
                    return False
                seen[5]-=1
            else:
                if seen[10] > 0 and seen[5] > 0:
                    seen[10]-=1
                    seen[5]-=1
                elif seen[10] <=0 and seen[5] >=2:
                    seen[5]-=2
                else:
                    return False
        return True


        