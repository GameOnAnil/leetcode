class Solution:
    def customSortString(self, order: str, s: str) -> str:
        set1 = Counter(s)
        set2 = Counter(s)
        res = []
        for o in order:
            if o in set2:
                while set2.get(o) > 0:
                    res.append(o)
                    set2[o]-=1
        for k,v in set2.items():
            while set2.get(k) > 0:
                res.append(k)
                set2[k]-=1
        return "".join(res)

        