class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def helper(index,path):
            if index == len(s):
                res.append(path[::])
                return
            for i in range(index,len(s)):
                print("index",index,i,"s:",s[index:i+1])
                if self.isPalindrome(s,index,i):
                    path.append(s[index:i+1])
                    helper(i + 1,path)
                    path.pop()
        helper(0,[])      
        return res

    def isPalindrome(self, s, start, end):
        while start <= end: # iterate through the substring
            if s[start] != s[end]: # check if current characters are not equal
                return False # if they are not, return false
            start += 1
            end -= 1
        return True
        