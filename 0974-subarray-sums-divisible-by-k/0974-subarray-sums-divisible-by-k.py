class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix, res = 0, 0
        for n in nums:
            prefix += n
            prefix %= k

            if prefix in count:
                res += count[prefix]
            count[prefix] += 1

        return res
