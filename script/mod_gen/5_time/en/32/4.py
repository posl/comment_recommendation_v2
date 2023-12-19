def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    result = []
    word_dict = set(words)
    for word in words:
        word_dict.remove(word)
        if isConcatenated(word, word_dict):
            result.append(word)
        word_dict.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()