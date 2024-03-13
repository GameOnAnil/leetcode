class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        res = 0
        while l < r:
            sum = nums[r]+nums[l]
            if sum < k:
                l+=1
            elif sum > k:
                r-=1
            else:
                res+=1
                l+=1
                r-=1
        return res

        