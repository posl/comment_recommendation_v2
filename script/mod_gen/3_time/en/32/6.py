def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    words_set = set()
    result = []
    for word in words:
        if wordBreak(word, words_set):
            result.append(word)
        words_set.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()