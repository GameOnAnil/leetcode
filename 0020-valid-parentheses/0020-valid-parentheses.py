class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        stack = []
        opening = set(["(", "[", "{"])
        for i in s:
            if not stack and i not in opening:
                return False
            if i in opening:
                stack.append(i)
            else:
                if (
                    (stack[-1] == "[" and i == "]")
                    or (stack[-1] == "(" and i == ")")
                    or (stack[-1] == "{" and i == "}")
                ):
                    stack.pop()
                else:
                    return False
        return True if not stack else False
