class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return N -1

        l,r = 1, N -2
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
        