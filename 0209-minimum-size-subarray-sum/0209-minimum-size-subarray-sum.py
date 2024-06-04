class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        INF = 10**9 + 1
        res = INF
        l = 0
        print(max(prefix))
        for r, p in enumerate(prefix):
            if p < target:
                continue
            
            while (prefix[r] - prefix[l]) >=target:
                l+=1
            # print("VALID",l,r,prefix[r],prefix[l])
            res = min(res,r-l+1)

        return res if res!=INF else 0


        