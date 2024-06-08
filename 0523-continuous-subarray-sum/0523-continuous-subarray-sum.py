class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N == 1:
            return False
        curr = 0
        seen = set()
        q = deque()
        q.append(0)
        for i in range(N):
            curr +=nums[i]
            curr %=k
            if curr in seen:
                return True
            q.append(curr)
            if len(q) > 1:
                seen.add(q.popleft())
        return False
        