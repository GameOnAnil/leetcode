class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        def dfs(curr,path):
            if not curr:
                res.append(path)
                # return
            for i in range(len(curr)):
                dfs(curr[:i] + curr[i+1:],path + [curr[i]])
        dfs(nums,[])
        return res

        