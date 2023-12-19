def findAllConcatenatedWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    wordSet = set(words)
    concatWords = []
    for word in words:
        wordSet.remove(word)
        if isConcatWord(word, wordSet):
            concatWords.append(word)
        wordSet.add(word)
    return concatWords

if __name__ == '__main__':
    findAllConcatenatedWords()