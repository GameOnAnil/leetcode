class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []
        for i in count1.keys():
            if i in count2:
                for _ in range(min(count1[i],count2[i])):
                    res.append(i)

        return res


        