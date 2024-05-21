class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,curr):
            res.append(curr)
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                dfs(j+1,curr+[nums[j]])

        dfs(0,[])
        return res
        