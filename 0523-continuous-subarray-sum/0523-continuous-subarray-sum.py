class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        seen = defaultdict(int)
        seen[0] = -1
        curr = 0
        for i in range(N):
            curr +=nums[i]
            curr %=k
            if curr in seen:
                if i-seen[curr]>=2:
                    # print("SEEN",seen[curr]+1,i)
                    return True
            else:
                seen[curr] = i

        return False
        