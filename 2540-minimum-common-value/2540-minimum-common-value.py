class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        count1, count2 = set(), set()
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                count1.add(nums1[i])
                if nums1[i] in count2:
                    return nums1[i]
            if i < len(nums2):
                count2.add(nums2[i])
                if nums2[i] in count1:
                    return nums2[i]
        return -1
