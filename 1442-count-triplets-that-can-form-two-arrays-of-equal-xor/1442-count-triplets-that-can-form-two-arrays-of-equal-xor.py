class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr) + 1
        res = 0
        prefix = [0] * N

        for i in range(1,N):
            prefix[i] = arr[i-1]^prefix[i-1]
        print(prefix)
        for i in range(N):
            for j in range(i+1,N):
                    if prefix[i] == prefix[j]:
                        res+= j - i - 1
        return res

        