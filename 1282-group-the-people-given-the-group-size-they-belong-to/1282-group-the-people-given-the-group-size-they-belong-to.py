class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = defaultdict(list[int])
        result = []
        for i , value in enumerate(groupSizes):
            g[value].append(i)
            if len(g[value]) == value:
                result.append(g[value])
                g[value] = []
        return result
        