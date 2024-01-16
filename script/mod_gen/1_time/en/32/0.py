class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        self.wordDict = set(words)
        self.memo = {}
        return [word for word in words if self.helper(word)]

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))