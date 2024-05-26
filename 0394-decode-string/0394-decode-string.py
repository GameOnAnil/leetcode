class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)
        res = []
        temp = []
        op = 0

        def get_num(s):
            curr= []
            while s and s[-1].isdigit():
                curr.append(s.pop())
            st = "".join(curr)
            return int(st[::-1])


        while s:
            curr = s.pop()
            if curr == "[":
                op-=1
                a = ("".join(temp)) * get_num(s)
                if op == 0:
                    res.append(a)
                    temp = []
                else:
                    temp = [a]
            elif curr =="]":
                if temp:
                    res.append("".join(temp))
                op+=1
                temp = []
            else:
                temp.append(curr)
        if temp:
            res.append("".join(temp))
        result = "".join(res)
        return result[::-1]

        