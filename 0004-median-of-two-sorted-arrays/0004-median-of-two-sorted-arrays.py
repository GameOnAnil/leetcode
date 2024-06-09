class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1, N2 = len(nums1), len(nums2)
        total = N1 + N2
        l,r = 0,0
        res =0
        m1,m2 = 0,0
        for _ in range(0,(N1+N2)//2+1):
            m2 = m1
            if l < N1 and r < N2:
                if nums1[l] > nums2[r]:
                    m1 = nums2[r]
                    r+=1
                else:
                    m1 = nums1[l]
                    l+=1
            elif l< N1:
                m1 = num1[l]
                l+=1
            else:
                m1 = nums2[r]
                r+=1
        if (total)%2 != 0:
            return float(m1)
        else:
            return (float(m1)+float(m2))/2.0

        