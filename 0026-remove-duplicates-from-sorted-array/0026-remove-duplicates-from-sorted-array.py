class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums
        l = 0
        r = 0
        count = 0
        while r < N:
            if r+1<N and nums[r] == nums[r+1]:
                while r+1<N and nums[r] == nums[r+1]:
                    r+=1
                nums[l] = nums[r]
                r+=1
                l+=1
            else:
                nums[l] = nums[r]
                l+=1
                r+=1
            count+=1
        return count


        