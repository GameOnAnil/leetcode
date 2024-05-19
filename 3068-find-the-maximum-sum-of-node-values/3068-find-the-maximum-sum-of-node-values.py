class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(n ^ k) - n for n in nums]
        res = sum(nums)
        delta.sort(reverse=True)

        for i in range(0,len(nums),2):
            if i == len(nums) - 1:
                break
            curr = delta[i] + delta[i+1]
            if curr > 0:
                res+=curr
        return res
