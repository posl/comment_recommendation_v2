def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    res = []
    words.sort(key=lambda x: len(x))
    wordSet = set()
    for word in words:
        if wordBreak(word, wordSet):
            res.append(word)
        wordSet.add(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()