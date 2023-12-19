def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words = set(words)
    cache = {}
    def dfs(word):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                cache[word] = True
                return True
            if prefix in words and dfs(suffix):
                cache[word] = True
                return True
        cache[word] = False
        return False
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
