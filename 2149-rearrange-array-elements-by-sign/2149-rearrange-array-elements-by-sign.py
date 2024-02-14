class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        res = []
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])
        return res
