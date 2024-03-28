class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        counter = defaultdict(int)
        for r in range(len(nums)):
            counter[nums[r]]+=1
            while counter[0] > k:
                counter[nums[l]]-=1
                l+=1
            res = max(r-l+1,res)
        return res
        