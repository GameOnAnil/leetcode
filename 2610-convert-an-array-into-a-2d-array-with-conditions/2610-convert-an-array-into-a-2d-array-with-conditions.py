class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(set)
        result = []
        for i, v in enumerate(nums):
            curr = 1
            while v in d[curr]:
                curr += 1
            d[curr].add(v)
        for j in d.values():
            if j != set():
                result.append(list(j))
        return result