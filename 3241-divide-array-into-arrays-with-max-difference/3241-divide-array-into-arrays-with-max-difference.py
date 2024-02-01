class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        if len(nums)<3: return []
        for i in range(0,len(nums),3):
            if (nums[i+2]-nums[i])<=k:
                result.append((nums[i],nums[i+1],nums[i+2]))
            else:
                return []
        return result
