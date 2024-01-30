class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)<3: return False
        for i in s:
            stack.append(i)
            if (len(stack)>=3) and (stack[-1] == "c" and stack[-2] == "b" and stack[-3] == "a"):
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack