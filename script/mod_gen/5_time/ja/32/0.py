class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        res = []
        dic = set()
        for word in words:
            if self.helper(word, dic):
                res.append(word)
            dic.add(word)
        return res

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))