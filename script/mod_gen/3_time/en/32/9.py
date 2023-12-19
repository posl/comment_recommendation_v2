def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    wordset = set(words)
    def dfs(word):
        for idx in range(1, len(word)):
            prefix = word[:idx]
            suffix = word[idx:]
            if prefix in wordset and suffix in wordset:
                return True
            if prefix in wordset and dfs(suffix):
                return True
        return False
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","catdogcat","catdogcatdog"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","catdogcat","catdogcatdog","catdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","catdogcat","catdogcatdog","catdogcatdogcat","catdogcatdogcatdog"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","catdogcat","catdogcatdog","catdogcatdogcat","catdogcatdogcatdog","catdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","catdogcat","catdogcatdog","catdogcatdogcat","catdogcatdogcatdog","catdogcatdogcatdogcat","catdogcatdogcatdogcatdog"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","catdogcat","catdogcatdog","catdogcatdogcat","catdogcatdogcatdog","catdogcatdogcatdogcat","catdogcatdogcatdogcatdog","catdogcatdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","catdogcat","catdogcatdog","catdogcatdogcat","catdogcatdogcatdog","catdogcat
