class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in range(0,len(sentences)):
            slist = sentences[i].split(" ")
            if len(slist) > max:
                max = len(slist)
        return max