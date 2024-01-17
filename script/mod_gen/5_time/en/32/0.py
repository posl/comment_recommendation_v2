class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        wordDict = set()
        result = []
        for word in words:
            if self.wordBreak(word, wordDict):
                result.append(word)
            wordDict.add(word)
        return result

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))