class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        seen = set()
        nums.sort()
        def dfs(i):
            if i == N:
                return 1
            curr = dfs(i + 1)

            if nums[i] - k not in seen:
                seen.add(nums[i])
                curr+=dfs(i + 1)
                seen.remove(nums[i])
            return curr

        
        res = dfs(0) - 1
        return res
        