class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)
        res = -1001
        for i in range(N):
            curr = energy[i]
            for j in range(i + k,N,k):
                curr+=energy[j]
            res = max(res,curr)
        return res

        