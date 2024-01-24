class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        o = {}
        for i in range(0,len(nums)):
            if nums[i] in o:
                o[nums[i]]+=1
            else:
                o[nums[i]]=1
        va = o.values()
        vlist = list(va)
        vlist.sort(reverse=True)
        vlist = vlist[:k]
        keys = [k for k, v in o.items() if v in vlist]
        return keys