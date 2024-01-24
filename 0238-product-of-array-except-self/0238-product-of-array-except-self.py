class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = []
        for i in range(0,len(nums)):
            if i == 0:
                left.append(1)
                continue
            left.append(left[-1]*nums[i-1])
        result =[]
        right = 1
        for i in reversed(range(len(nums))):
            l =left[i]
            if i == len(nums)-1:
                result.insert(0,l*right)
            else:
                right =right*nums[i+1]
                result.insert(0,l*right)
        return result