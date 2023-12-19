def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key = lambda x: len(x))
    wordSet = set()
    result = []
    for word in words:
        if wordBreak(word, wordSet):
            result.append(word)
        wordSet.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()