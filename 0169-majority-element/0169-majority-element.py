class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = defaultdict(int)
        for i in nums:
            data[i]+=1
        
        for i,v in data.items():
            if v>= (len(nums)/2):
                return i
        return -1
        