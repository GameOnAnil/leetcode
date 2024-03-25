class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for n in nums:
            if n in seen:
                res.append(n)
            seen.add(n)
        return res

        