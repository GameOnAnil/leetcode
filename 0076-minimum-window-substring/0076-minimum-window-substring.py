class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count = defaultdict(int)
        for i in t:
            count[i]-=1

        res = ""
        print(count)
        for r, v in enumerate(s):
            count[v]+=1
            # print(r,count)
            if min(count.values()) < 0:
                continue
            while l < r:
                count[s[l]]-=1
                if count[s[l]] <0:
                    count[s[l]]+=1
                    break
                l+=1
            curr = s[l:r+1]
            if res:
                res = curr if len(curr)<=len(res) else res
            else:
                res = curr
        return res



        