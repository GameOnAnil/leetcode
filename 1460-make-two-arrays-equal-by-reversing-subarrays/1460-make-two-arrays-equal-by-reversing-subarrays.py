class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return set(target) == set(arr)
        