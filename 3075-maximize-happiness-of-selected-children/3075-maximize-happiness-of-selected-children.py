class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        count = 0
        res = 0
        for i in happiness:
            if count >= k:
                break
            if i - count <= 0:
                break
            res += i - count
            count +=1
        return res

        