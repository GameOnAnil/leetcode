class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        prev = 0
        for v in sorted(count.values()):
            if v == prev:
                return False
            prev = v
        return True

        