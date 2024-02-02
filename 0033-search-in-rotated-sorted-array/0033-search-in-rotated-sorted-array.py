class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[l]:
                return l
            if target == nums[mid]:
                return mid
            if target == nums[r]:
                return r
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1 
            else:
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1 

        return -1 
