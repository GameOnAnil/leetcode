class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1: return 1
        if not trust and n >1: return -1
        data = defaultdict(int)
        notTrusted = set()
        for i in trust:
            data[i[1]]+=1
            notTrusted.add(i[0])
        for i, v in data.items():
            if (v == n-1) and i not in notTrusted:
                return i
        return -1
        