class Solution:
    def numWaterBottles(self, num: int, e: int) -> int:
        curr = 0

        while num >= e:
            curr += e
            num -= e
            num+=1
        return curr + num
        