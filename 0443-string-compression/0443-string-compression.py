class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)<=1:
            return len(chars)
        l = r = 0
        chars.append(0)
        curr = chars[0]
        res = []
        while r < len(chars):
            if curr == chars[r]:
                r+=1
            else:
                res.append(chars[l])
                if (r-l) > 1:
                    res.extend(list(str(r-l)))
                l = r
                curr = chars[r]
        while len(chars) > len(res):
            chars.pop()
        for i,v in enumerate(res):
            chars[i] = v
        return len(chars)

            

            

        