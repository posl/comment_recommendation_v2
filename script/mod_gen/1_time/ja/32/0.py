class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        dp = set()
        res = []
        for word in words:
            if self.wordBreak(word, dp):
                res.append(word)
            dp.add(word)
        return res

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))