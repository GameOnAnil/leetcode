class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)

        for i,v in nums1:
            mp[i] = v

        for i, v in nums2:
            mp[i]+=v

        ans = []

        for k,v in sorted(mp.items()):
            ans.append([k,v])

        return ans
