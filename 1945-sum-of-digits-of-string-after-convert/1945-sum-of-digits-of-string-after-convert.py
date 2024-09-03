class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)
        
        for i in range(k):
            curr = 0
            for d in numeric_string:
                curr+=int(d)
            numeric_string = str(curr)

        return int(numeric_string)
