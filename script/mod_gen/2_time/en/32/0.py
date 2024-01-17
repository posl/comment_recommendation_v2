class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key = len)
        ans = []
        word_set = set(words)
        for word in words:
            word_set.remove(word)
            if self.helper(word, word_set):
                ans.append(word)
            word_set.add(word)
        return ans

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))