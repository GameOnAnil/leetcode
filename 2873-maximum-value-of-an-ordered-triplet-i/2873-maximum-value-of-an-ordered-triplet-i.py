class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        cmax = 0
        dif = 0
        ans = 0

        for i in range(3):
            cmax = max(nums[i], cmax)
            dif = max(dif, (cmax - nums[i]))
        ans = max(ans, (nums[0] - nums[1]) * nums[2])

        for i in range(3, len(nums)):
            ans = max(ans, dif * nums[i])
            cmax = max(nums[i], cmax)
            dif = max(dif, (cmax - nums[i]))

        return ans
