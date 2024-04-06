class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                continue
            if c == ")":
                if not stack:
                    s[i] = ""
                else:
                    stack.pop()
        while stack:
            index = stack.pop()
            s[index] = ""
        return "".join(s)
            