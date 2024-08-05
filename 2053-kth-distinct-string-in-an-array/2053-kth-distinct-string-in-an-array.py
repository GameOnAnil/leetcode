class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = set()
        dup = set()
        for a in arr:
            if a not in seen:
                seen.add(a)
            else:
                dup.add(a)

        for a in arr:
            if a not in dup:
                k-=1
            if k == 0:
                return a 
        return ""