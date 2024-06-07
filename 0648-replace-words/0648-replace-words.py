class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        res = []
        sentence = list(sentence.split(" "))
        for s in sentence:
            for i in range(len(s)):
                curr = s[:i+1]
                # print("Check",curr)
                if curr in dictionary:
                    # print("found")
                    res.append(curr)
                    break
                if i == len(s)-1:
                    res.append(s)
        print(res)
        return " ".join(res)

        