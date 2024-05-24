class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], scores: List[int]
    ) -> int:
        N = len(words)
        l_count = collections.Counter(letters)
        res = 0

        @cache
        def get_score(index):
            w = Counter(words[index])
            score = 0
            for c, v in w.items():
                c = ord(c) - ord("a")
                score+=scores[c] * v
            return score

        def dfs(index,counts):
            if index == N:
                return 0
            # dont include
            best = 0
            best = max(best,dfs(index + 1,counts))
            # include
            f = Counter(words[index])
            if counts> f:
                score = get_score(index) 
                counts -= f
                best =max(best,dfs(index + 1,counts) + score)
                counts += f

            return best
        return dfs(0,l_count)