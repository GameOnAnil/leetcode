class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []

        for a in arr2:
            if a in count:
                for _ in range(count[a]):
                    res.append(a)
                del count[a]
        for k,v in sorted(count.items()):
            if v>0:
                for _ in range(v):
                    res.append(k)
        return res



        