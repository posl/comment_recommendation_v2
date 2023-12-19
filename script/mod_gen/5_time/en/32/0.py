def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words = set(words)
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                return True
            if prefix in words and dfs(suffix):
                return True
            if suffix in words and dfs(prefix):
                return True
        return False
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat","catdogcatdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat","catdogcatdogcatdogcatdogcat","catdogcatdogcatdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat","catdogcatdogcatdogcatdogcat","catdogcatdogcatdogcatdogcatdogcat","catdogcatdogcatdogcatdogcatdogcatdogcat"]))
print("The arrays above should be [\"catsdog

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()