class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        P = len(potions)
        S = len(spells)
        potions.sort()
        res = [0] * S

        def findPivot(num):
            l,r = 0, P-1 
            currbest = P
            while l<=r:
                mid = (l+r)//2
                if potions[mid] < num:
                    l = mid + 1                  
                else:
                    currbest = mid
                    r = mid - 1  
            return currbest

        for i, s in enumerate(spells):
            pivot = findPivot((success + s - 1) // s)
            res[i] = P - pivot
        return res


        