def findAllConcatenatedWordsInADict(words):
    words.sort(key=lambda x: len(x))
    print(words)
    result = []
    wordSet = set()
    for word in words:
        if wordBreak(word, wordSet):
            result.append(word)
        wordSet.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()