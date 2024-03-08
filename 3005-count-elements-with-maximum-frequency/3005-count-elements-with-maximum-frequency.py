class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        res = 0
        currMax = 0
        sortedList = sorted(count.values(), reverse=True)
        r = 0
        while r < len(sortedList) and sortedList[0] == sortedList[r]:
            r += 1
        return r * sortedList[0]
