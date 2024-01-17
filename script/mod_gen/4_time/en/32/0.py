class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        wordDict = set()
        res = []
        for word in words:
            if self.canForm(word, wordDict):
                res.append(word)
            wordDict.add(word)
        return res

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))