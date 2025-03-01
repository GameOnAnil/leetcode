class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        for i in range(N - 1):
            j = i + 1
            while nums[i] == 0 and j < N:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                else:
                    j += 1

        return nums
