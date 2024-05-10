class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        tmap = defaultdict(float)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                temp = arr[i]/arr[j]
                tmap[(arr[i],arr[j])] = temp
        sortedmap = dict(sorted(tmap.items(), key=lambda item: item[1]))
        keys_list = list(sortedmap.keys())
        return list(keys_list[k-1])

        