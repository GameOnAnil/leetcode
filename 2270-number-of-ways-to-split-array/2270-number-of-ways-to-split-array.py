class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0] * N
        suffix = [0] * N

        for i, v in enumerate(nums):
            if i == 0:
                prefix[i] = v
                suffix[N - 1] = nums[N - 1]
            else:
                prefix[i] = prefix[i-1] + v
                suffix[N - 1 - i] = suffix[N - i] + nums[N - 1 - i]
        ans = 0

        for i in range(N-1):
            if prefix[i] >= suffix[i+1]:
                ans+=1

        return ans

        