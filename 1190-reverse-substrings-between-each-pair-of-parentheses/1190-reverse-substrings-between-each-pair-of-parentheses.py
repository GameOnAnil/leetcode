class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ")":
                stack.append(c)
            else:
                # print("stack",stack)
                temp = []
                while stack:
                    a = stack.pop()
                    if a == "(":
                        stack+=temp
                        break
                    else:
                        temp.append(a)
                continue
        return "".join(stack)
                    

        