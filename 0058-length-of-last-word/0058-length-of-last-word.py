class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=r=0
        s = s.strip()
        while r< len(s):
            if s[r] == " ":
                l = r+1
            r+=1 
        return len(s[l:])


        