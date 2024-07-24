class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mp = {i: v for i, v in enumerate(mapping)}
        res = []
        for i, v in enumerate(nums):
            curr = list(str(v))
            for j in range(len(curr)):
                temp = curr[j]
                curr[j] = str(mp[int(temp)])
            res.append((int("".join(curr)), nums[i],i))
        res.sort(key=lambda x: [x[0], x[2]])
        return [i for _, i, __ in res]
