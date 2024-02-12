class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        print(nums)
        m = defaultdict(int)
        for i, v in enumerate(nums):
            if (target - v) in m:
                return [i, m.get(target - v)]
            else:
                m[v] = i
        return []
