class Solution:
    def reverseWords(self, s: str) -> str:
        clean_text = re.sub(r'\s+', ' ', s)
        splited =  clean_text.split()
        return " ".join(splited[::-1])
        # l = r = 0
        # words = []
        # while r < len():
        #     if s[r]!="":
        #         r+=1
        #     else:
        #         words.append(s[l:r+1])
        #         while s[l] == "":
        #             l+=1
        #         r = l + 1


        