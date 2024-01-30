class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in tokens:
            if i == "+":
                result.append(result.pop() + result.pop())
            elif i == "-":
                r1,r2 = result.pop(),result.pop()
                result.append(r2 - r1)
            elif i == "*":
                result.append(result.pop() * result.pop())
            elif i == "/":
                r1,r2 = result.pop(),result.pop()
                result.append(int(r2 / r1))
            else:
                result.append(int(i))
        return result[-1]
