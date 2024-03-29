class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = res = curr = 0
        max_element = max(nums)
        for r in range(len(nums)):
            if nums[r] == max_element:
                curr+=1
            while curr == k:
                if nums[l] == max_element:
                    curr-=1
                l+=1
            res+=l
        return res

        