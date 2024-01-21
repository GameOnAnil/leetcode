class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c= 0
        for i in items:
            if (ruleKey == "type" and i[0]==ruleValue) or (ruleKey == "color" and i[1]==ruleValue) or (ruleKey == "name" and i[2]==ruleValue):
                c += 1
        return c
        