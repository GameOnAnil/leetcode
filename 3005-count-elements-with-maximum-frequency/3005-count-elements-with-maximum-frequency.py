class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = max(counter.values())
        res = 0
        for i in counter.values():
            if i == max_freq:
                res+=i
        return res
