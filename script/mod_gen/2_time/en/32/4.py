def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, start, wordDict):
        if start == len(word):
            return True
        for i in range(start, len(word)):
            if word[start:i+1] in wordDict and dfs(word, i+1, wordDict):
                return True
        return False
    
    wordDict = set(words)
    res = []
    for word in words:
        wordDict.remove(word)
        if dfs(word, 0, wordDict):
            res.append(word)
        wordDict.add(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()