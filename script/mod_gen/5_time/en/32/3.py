def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    result = []
    wordDict = set()
    for word in words:
        if canForm(word, wordDict):
            result.append(word)
        wordDict.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()