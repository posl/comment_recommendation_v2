def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordDict, memo):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict:
                if suffix in wordDict or dfs(suffix, wordDict, memo):
                    memo[word] = True
                    return True
        memo[word] = False
        return False
    wordDict = set(words)
    memo = {}
    return [word for word in words if dfs(word, wordDict, memo)]

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()