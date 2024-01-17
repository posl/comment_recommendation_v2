class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        def dfs(word: str, word_set: set[str], memo: dict[str, bool]) -> bool:
            if word in memo:
                return memo[word]
            for index in range(1, len(word)):
                prefix = word[:index]
                suffix = word[index:]
                if prefix in word_set and suffix in word_set:
                    memo[word] = True
                    return True
                if prefix in word_set and dfs(suffix, word_set, memo):
                    memo[word] = True
                    return True
                if suffix in word_set and dfs(prefix, word_set, memo):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        word_set = set(words)
        memo = {}
        return [word for word in words if dfs(word, word_set, memo)]

if __name__ == '__main__':
    words = input().split()
    a = Solution()
    print(a.findAllConcatenatedWordsInADict(words))