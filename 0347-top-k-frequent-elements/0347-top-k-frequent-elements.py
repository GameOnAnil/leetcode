class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        o = {}
        for i in range(0,len(nums)):
            if nums[i] in o:
                o[nums[i]]+=1
            else:
                o[nums[i]]=1
        kthItems =sorted(o, key=o.get, reverse=True)[:k]
        return kthItems