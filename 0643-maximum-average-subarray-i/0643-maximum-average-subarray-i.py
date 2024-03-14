class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr= 0
        res = 0
        for i in range(k):
            curr+=nums[i]
        res = curr/k
        l,r = 1, k 
        while r < len(nums):
            curr = curr - nums[l-1] + nums[r]
            res = max(res,curr/k)
            l+=1
            r+=1
        return res



        