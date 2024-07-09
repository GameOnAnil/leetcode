class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        last = customers[0][0]
        for a,d in customers:
            if a <=last:
                curr = last + d
            else:
                curr = a + d
            diff = curr - a
            res += diff
            last = curr
        return res/len(customers)



        