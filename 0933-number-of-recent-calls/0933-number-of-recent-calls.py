class RecentCounter:

    def __init__(self):
        self.data = []
        

    def ping(self, t: int) -> int:
        self.data.append(t)
        temp = self.data.copy()
        count = 0
        ra = [t-3000,t]
        while temp:
            a = temp.pop()
            if a< ra[0] or a > ra[1] :
                return count
            count+=1
        return count

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)