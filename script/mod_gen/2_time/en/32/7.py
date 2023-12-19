def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    res = []
    wordset = set()
    for word in words:
        if canForm(word, wordset):
            res.append(word)
        wordset.add(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()