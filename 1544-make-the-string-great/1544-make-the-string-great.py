class Solution:
    def makeGood(self, s: str) -> str:
        temp = []
        for i in s:
            if not temp:
                temp.append(i)
                continue
            first = ord(temp[-1])
            second = ord(i)
            asci_diff = abs(first - second)
            if asci_diff == 32:
                temp.pop()
            else:
                temp.append(i)
        return "".join(temp)
            
        