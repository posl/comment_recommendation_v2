def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    wordDict = set()
    result = []
    for word in words:
        if wordBreak(word, wordDict):
            result.append(word)
        wordDict.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()