class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key = len)
        res = []
        wordset = set()
        for word in words:
            if self.dfs(word, wordset):
                res.append(word)
            wordset.add(word)
        return res

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))