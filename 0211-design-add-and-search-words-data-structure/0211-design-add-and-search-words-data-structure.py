class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            curr = root
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.child.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]
            return curr.word

        return dfs(0, self.root)
