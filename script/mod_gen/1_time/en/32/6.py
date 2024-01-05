def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    wordDict = set(words)
    def dfs(word):
        for i in range(1,len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict and suffix in wordDict:
                return True
            if prefix in wordDict and dfs(suffix):
                return True
            if suffix in wordDict and dfs(prefix):
                return True
        return False
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res

if __name__ == '__main__':
    words = input().split()
    a = findAllConcatenatedWordsInADict(words)
    print(a)