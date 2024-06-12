class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0]*3
        for n in nums:
            bucket[n]+=1
        index = 0
        for i,v in enumerate(bucket):
            for _ in range(v):
                nums[index] =i
                index+=1


        