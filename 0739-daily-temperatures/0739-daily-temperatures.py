class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                lastIndex, lastValue = stack.pop()
                result[lastIndex] = i - lastIndex
            stack.append((i, n))
        return result
