class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = r = 0
        res = 0
        seen  = defaultdict(int)
        while l < len(nums):
            if nums[l] != minK:
                l += 1
                r = 0
                continue
            while r < len(nums):
                if nums[r] == maxK:
                    if (str((l,r)) not in seen) and (str((r,l)) not in seen):
                        res += 1
                        seen[str((l,r))]+=1
                r += 1
            l += 1
            r = 0
        return res
