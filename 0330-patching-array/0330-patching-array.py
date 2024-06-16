class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        reachable = 0  # This represents the maximum sum that can be formed using patches
        
        i = 0
        while reachable < n:
            if i < len(nums) and nums[i] <= reachable + 1:
                reachable += nums[i]
                i += 1
            else:
                patches += 1
                reachable += reachable + 1
        
        return patches