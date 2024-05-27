class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        for i in range(max(nums) +1 ):
            l = 0
            while l < len(nums) and nums[l] < i:
                l+=1
            sub = nums[l:]
            print(i,l)
            if len(sub) == i:
                return i
        return -1

        