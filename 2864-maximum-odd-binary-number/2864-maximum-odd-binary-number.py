class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        onesCount = 0
        res = ""
        for i in s:
            if i == "1":
                onesCount += 1
        for j in range(len(s)):
            if (onesCount > 1 and j != (len(s) - 1)) or (
                j == (len(s) - 1) and onesCount == 1
            ):
                res += "1"
                onesCount -= 1
            else:
                res += "0"
        return res
