class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res =[]
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[::])
                return
            for k, v in counter.items():
                if v > 0:
                    counter[k]-=1
                    dfs(path + [k])
                    counter[k]+=1
        dfs([])
        return res
        