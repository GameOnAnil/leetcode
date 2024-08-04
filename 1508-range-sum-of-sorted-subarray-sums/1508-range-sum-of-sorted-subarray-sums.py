class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        sumArr = []
        N = len(nums)

        for i in range(N):
            curr = []
            prev = 0
            for j in range(i,N):
                prev +=nums[j]
                curr.append(prev)
            sumArr.extend(curr)

        sumArr.sort()
        # print(sumArr[left-1:right])
        return sum(sumArr[left-1:right])%MOD
        