class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       m = {}
       for i in range(0,len(nums)):
            if (target - nums[i]) in m:
               return [nums.index(target-nums[i]),i]
            else:
               m[nums[i]] = i
       return []



        