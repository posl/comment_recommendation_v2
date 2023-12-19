def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    res = []
    wordSet = set(words)
    
    for word in words:
        wordSet.remove(word)
        if word:
            if dfs(word, wordSet, {}):
                res.append(word)
        wordSet.add(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()