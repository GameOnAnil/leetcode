class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen = defaultdict(int)
        rows = len(nums)
        for i in range(rows):
            for j in range(len(nums[i])):
                seen[nums[i][j]]+=1
        res = []
        for k,v  in seen.items():
            if v == rows:
                res.append(k)
        res.sort()
        return res

        