class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = []
        for p,s in zip(position,speed):
            comb.append([p,s])
        comb = sorted(comb,key = lambda x:x[0])
        print(comb)

        res = 0
        l = 0
        while l < len(comb):
            curr = comb[l]
            r = l
            while (r+1) < len(comb) and comb[r+1][1] <= curr[1]:
                r+=1
            curr = [curr[0],min(curr[1],comb[r][1])]
            l = r+1
            res+=1

        return res

        