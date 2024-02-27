class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def dfs(i,path):
            if i == len(digits):
                res.append(path)
                return
            for j in dic[digits[i]]:
                dfs(i + 1,path + j)
        dfs(0,"")
        return res