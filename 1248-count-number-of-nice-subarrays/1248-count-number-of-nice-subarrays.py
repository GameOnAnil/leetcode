class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0]+=1
        res = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]%2
            if (curr_sum-k) in prefix:
                res+= prefix[curr_sum-k]
            prefix[curr_sum] += 1
        return res

            

            