class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start = 0
        prefix_zeros = 0
        win_sum = 0
        res = 0
        
        for end, num in enumerate(nums):
            win_sum += num
            
            while start < end and (nums[start] == 0 or win_sum > goal):
                if nums[start] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1
                    
                win_sum -= nums[start]
                start += 1
                
            if win_sum == goal:
                res += 1 + prefix_zeros
                
        return res