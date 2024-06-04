class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        oddSeen = False
        res = 0
        for k,i in count.items():
            if i%2==0:
                res+=i
            else:
                curr = count.get(k)
                if curr >0:
                    oddSeen =True
                    res+=curr-1
        if oddSeen:
            res+=1
        return res