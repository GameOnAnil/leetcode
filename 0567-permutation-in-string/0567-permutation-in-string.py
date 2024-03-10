class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return
        count = Counter(s1)
        l,r = 0, len(s1)-1
        while r < len(s2):
            inner_counter = Counter(s2[l:r+1])
            if  inner_counter == count:
                return True
            r+=1
            l+=1
        return False




        