class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, gain):
            stack = []
            points = 0
            for c in s:
                if c == second and stack and stack[-1] == first:
                    stack.pop()
                    points += gain
                else:
                    stack.append(c)
            return "".join(stack), points
        
        res = 0
        
        if x > y:
            # Remove "ab" first
            s, points = remove_substring(s, 'a', 'b', x)
            res += points
            # Then remove "ba"
            s, points = remove_substring(s, 'b', 'a', y)
            res += points
        else:
            # Remove "ba" first
            s, points = remove_substring(s, 'b', 'a', y)
            res += points
            # Then remove "ab"
            s, points = remove_substring(s, 'a', 'b', x)
            res += points
        
        return res