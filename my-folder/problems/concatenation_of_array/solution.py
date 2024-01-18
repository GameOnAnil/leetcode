class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            ans.insert(i,nums[i])
            ans.insert(i+len(nums),nums[i])
        return ans
        