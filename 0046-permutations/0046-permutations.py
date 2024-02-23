class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res) -> None:
        # Base case
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            newPath = path + [nums[i]]
            newNum = nums[:i] + nums[i + 1 :]
            self.dfs(newNum, newPath, res)
