class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        def find_greater(num,i):
            l,r = 0,len(nums)-1
            curr = len(nums)
            while l <= r:
                mid = (l+r)//2
                if nums[mid] >= i:
                    curr = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return curr
        N = len(nums)
        for i in range(N + 1):
            curr = find_greater(nums,i)
            if i == len(nums[curr:]):
                return i
        return -1

                    
        