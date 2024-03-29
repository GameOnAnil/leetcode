class TimeMap:

    def __init__(self):
        self.di = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.di[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.di.get(key,[])
        if not values: return result
        l, r = 0, len(values)-1
        while l<=r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)