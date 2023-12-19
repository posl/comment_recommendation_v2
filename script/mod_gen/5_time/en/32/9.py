def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    words_set, res = set(), []
    for word in words:
        if wordBreak(word, words_set):
            res.append(word)
        words_set.add(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()