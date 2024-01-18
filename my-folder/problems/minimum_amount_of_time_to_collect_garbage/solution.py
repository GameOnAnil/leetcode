class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        pMaxIndex = 0
        gMaxIndex = 0
        mMaxIndex = 0
        for i in range(0,len(garbage)):
            if "P" in garbage[i]:
                pMaxIndex = i
                total += garbage[i].count("P") 
            if "G" in garbage[i]:
                gMaxIndex = i
                total += garbage[i].count("G")
            if "M" in garbage[i]:
                mMaxIndex = i
                total += garbage[i].count("M")

        total += sum(travel[:pMaxIndex])
        total += sum(travel[:gMaxIndex])
        total += sum(travel[:mMaxIndex])

        return  total
            


