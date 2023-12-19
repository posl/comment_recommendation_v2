def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordSet, memo):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordSet and suffix in wordSet:
                memo[word] = True
                return True
            if prefix in wordSet and dfs(suffix, wordSet, memo):
                memo[word] = True
                return True
        memo[word] = False
        return False
    wordSet = set(words)
    memo = {}
    ans = []
    for word in words:
        if dfs(word, wordSet, memo):
            ans.append(word)
    return ans

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()