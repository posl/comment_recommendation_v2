def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordDict):
        if word in wordDict:
            return wordDict[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict and wordDict[prefix] and dfs(suffix, wordDict):
                wordDict[word] = True
                return True
        wordDict[word] = False
        return False
    
    wordDict = {}
    for word in words:
        wordDict[word] = True
    res = []
    for word in words:
        wordDict[word] = False
        if dfs(word, wordDict):
            res.append(word)
    return res
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","dog","catdog"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
