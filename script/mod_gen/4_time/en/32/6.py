def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def helper(word, wordDict):
        if word in wordDict:
            return wordDict[word]
        for i in range(1, len(word)):
            if word[:i] in wordDict:
                if word[i:] in wordDict[word[:i]] or helper(word[i:], wordDict):
                    wordDict[word] = True
                    return True
        wordDict[word] = False
        return False
    wordDict = {}
    words.sort(key=len)
    res = []
    for word in words:
        if helper(word, wordDict):
            res.append(word)
    return res
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
