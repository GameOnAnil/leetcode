class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        if not citations:
            return 0
        l,r = 0, N - 1
        while l <= r:
            mid = l + (r-l)//2
            curr = N - mid
            if citations[mid] == curr:
                return citations[mid]
            elif citations[mid] > curr:
                r = mid - 1
            else:
                l = mid + 1
        return N - l
            
        