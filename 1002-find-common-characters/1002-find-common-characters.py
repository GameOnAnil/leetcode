class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        prev = Counter(words[0])
        for i in range(1,len(words)):
            counter = Counter(words[i])
            prev = prev & counter
        common_chars = ''.join([char * prev[char] for char in prev])
        return list(common_chars)
        