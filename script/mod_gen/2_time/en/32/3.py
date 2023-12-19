def findAllConcatenatedWordsInADict(words):
    words.sort(key=len)
    result = []
    wordDict = set()
    for word in words:
        if wordBreak(word, wordDict):
            result.append(word)
        wordDict.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()