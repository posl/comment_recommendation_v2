def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    res = []
    words = set(words)
    for word in words:
        words.remove(word)
        if isConcatenated(word, words):
            res.append(word)
        words.add(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()