class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        if (len(s)==1 and (s[0]!="(" 
        or s[0]!="{" or s[0]!="[")):
            return False 
        for i in s:
            if i == "(" or i=="{" or i=="[":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                l = stack.pop()
                if l=="(" and  i !=")":
                    return False
                elif l=="{" and i !="}":
                    return False
                elif l=="[" and i !="]":
                    return False
        return len(stack)==0