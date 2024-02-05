class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prevSum, result = 0, 0
        if len(arr) < 3:
            return 0
        for i in range(k):
            prevSum += arr[i]
        if (prevSum / k) >= threshold:
            result += 1
        l, r = 0, k
        while r < len(arr):
            prevSum = prevSum + arr[r] - arr[l]
            if (prevSum / k) >= threshold:
                result += 1
            l += 1
            r += 1
        return result
