class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindow(nums, k)

    def slidingWindow(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l1, l2, total = 0, 0, 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while len(freq) > k:
                freq[nums[l2]] -= 1
                if freq[nums[l2]] == 0:
                    del freq[nums[l2]]
                l2 += 1
                l1 = l2

            while freq[nums[l2]] > 1:
                freq[nums[l2]] -= 1
                l2 += 1
            if len(freq) == k:
                total += l2 - l1 + 1
        return total
