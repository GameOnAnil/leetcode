class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        list = []
        for i in range(0,len(words)):
            if words[i].__contains__(x):
                list.append(i)
        return list
        