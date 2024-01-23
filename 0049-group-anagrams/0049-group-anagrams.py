class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sortedList = []
        r= {}
        for i in range(0,len(strs)):
            sortedList.append("".join(sorted(strs[i])))
        for i in range(0,len(sortedList)):
            if not r.__contains__(sortedList[i]):
                r[sortedList[i]]=[strs[i]]
            else:
                prev = r.get(sortedList[i])
                prev.append(strs[i])
                r[sortedList[i]]=prev
        return r.values()

        