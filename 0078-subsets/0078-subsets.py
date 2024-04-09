class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0,nums,[],res)
        return res
    def dfs(self,i,nums,path,res):
        print(path)
        if i == len(nums):
            res.append(path)
            return
        self.dfs(i+1,nums,path+[nums[i]],res)
        self.dfs(i+1,nums,path,res)

        