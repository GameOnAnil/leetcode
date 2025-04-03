class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        cmax = 0
        dif = 0
        ans = 0

        for i in range(len(nums)):
            ans = max(ans, dif * nums[i])
            cmax = max(nums[i], cmax)
            dif = max(dif, (cmax - nums[i]))

        return ans
