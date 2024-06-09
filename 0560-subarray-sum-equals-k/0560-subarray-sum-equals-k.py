class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix, res = 0, 0
        for n in nums:
            prefix += n
            r = prefix - k
                
            res += count[r]
            count[prefix] += 1
        # print(count)
        return res
