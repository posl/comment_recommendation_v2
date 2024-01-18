class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        result = []
        word_set = set()
        for word in words:
            if self.helper(word, word_set):
                result.append(word)
            word_set.add(word)
        return result

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))