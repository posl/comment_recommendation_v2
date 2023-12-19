def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordSet, cache):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordSet and suffix in wordSet:
                cache[word] = True
                return True
            if prefix in wordSet and dfs(suffix, wordSet, cache):
                cache[word] = True
                return True
        cache[word] = False
        return False
    wordSet = set(words)
    cache = {}
    res = []
    for word in words:
        if dfs(word, wordSet, cache):
            res.append(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()