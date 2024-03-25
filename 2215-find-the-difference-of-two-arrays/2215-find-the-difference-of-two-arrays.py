class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1,s2 = set(nums1),set(nums2)
        dif1 = s1 - s2
        dif2 = s2 - s1
        return [list(dif1),list(dif2)]
        