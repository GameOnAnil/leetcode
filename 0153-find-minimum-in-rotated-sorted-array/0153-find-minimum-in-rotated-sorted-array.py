class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, result = 0, len(nums) - 1, nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result,nums[l])
                break
            mid = (l + r) // 2
            result = min(result,nums[mid])
            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return result
